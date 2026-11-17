# ADR-0005: Integração de Firewall Físico Cisco ASA 5506-X e Servidor DHCP Dedicado

**Date**: 2026-11-10  
**Status**: accepted  
**Deciders**: Diogo Santos Pires Jandiroba (Lead Solutions Architect)  

## Context

No modelo inicial de segmentação lógica (registrado nos ADR-0002 e ADR-0004), o roteador interno Cisco 2911 acumulava a função de concentrador *Router-on-a-Stick*, servidor DHCP local para as estações de trabalho e rede sem fio, e ponto de aplicação de listas de controle de acesso (ACLs). 

Embora suficiente para a escala imediata de 97 pontos, a centralização de múltiplos papéis no mesmo ativo de roteamento introduz acoplamento operacional e limita a escalabilidade da rede quando submetida ao crescimento de conexões simultâneas ou necessidade de inspeção avançada de pacotes. Buscou-se desacoplar os serviços de atribuição de rede e estabelecer uma barreira de segurança perimetral com inspeção de estado dedicada (*stateful inspection*).

## Decision

Evoluir a arquitetura lógica e física da rede através da introdução de dois novos componentes dedicados:

1. **Firewall Perimetral Físico (Cisco ASA 5506-X)**:
   - Posicionado entre o roteador de borda (`router_border` - Cisco ISR 4321) e o roteador interno de distribuição (`router_interno` - Cisco 2911);
   - Interface Externa (`GigabitEthernet1/1` - *outside*, nível de segurança 0): Conectada ao `router_border` via enlace ponto a ponto `10.0.0.0/30` (IP `10.0.0.2`);
   - Interface Interna (`GigabitEthernet1/2` - *inside*, nível de segurança 100): Conectada ao `router_interno` via novo enlace ponto a ponto `10.0.1.0/30` (IP `10.0.1.1`);
   - Habilitação da inspeção de estado via *Modular Policy Framework* (MPF) para protocolos ICMP, HTTP e DNS.

2. **Servidor DHCP Dedicado (`SRV-DHCP`)**:
   - Alocado na VLAN 20 (DMZ / Servidores) com endereço estático `192.168.20.30/24` e gateway `192.168.20.1`;
   - Centraliza o gerenciamento dos *pools* de endereçamento dinâmico da rede de pesquisa (`192.168.30.0/24`) e da rede Wi-Fi (`192.168.40.0/24`);
   - Configuração do serviço de retransmissão (*DHCP Relay*) no roteador Cisco 2911 via comando `ip helper-address 192.168.20.30` nas subinterfaces `GigabitEthernet0/0.30` e `GigabitEthernet0/0.40`.

3. **Rejeição de Switches Individuais por Servidor**:
   - Manutenção de um switch de agregação corporativo único (`SW-CT12`) para a sala de servidores e estações locais, descartando a alocação de um switch físico exclusivo por servidor devido ao desperdício de portas (subutilização de mais de 90% da capacidade de portas L2) e aumento ineficiente de consumo energético e unidades de rack.

4. **Emulação do Provedor WAN / Internet (`ISP-UFS`)**:
   - Inclusão de um roteador dedicado (`ISP-UFS` - Cisco 2911) no bloco externo para terminação do enlace WAN institucional `200.17.0.0/30` (IP `200.17.0.1`) e interface virtual `Loopback0` (`8.8.8.8/32`), permitindo a validação experimental fim a fim da tradução NAT/PAT do `router_border` e da inspeção de conexões no ASA a partir de qualquer estação interna.

## Alternatives Considered

### Alternative 1: Manutenção dos Serviços Integrados no Cisco 2911 (Status Quo)
- **Pros**: Zero alteração em cabeamento e menor número de equipamentos para gerenciar no simulador.
- **Cons**: Processamento de requisições DHCP concorre com o tráfego de comutação inter-VLAN; ACLs estendidas em roteadores não oferecem a profundidade de inspeção de um firewall de estado dedicado.
- **Why not**: O projeto visa demonstrar máxima maturidade arquitetural e aderência aos padrões de infraestrutura de alta confiabilidade.

### Alternative 2: Switch Físico Dedicado para Cada Servidor
- **Pros**: Isolamento elétrico e físico estrito entre os servidores da aplicação.
- **Cons**: Desperdício de 22 de 24 portas por switch; consumo multiplicado de portas de energia (PDU), espaço de rack (RU) e patch cords; encarecimento injustificável na planilha orçamentária do PNCP.
- **Why not**: Prática condenada pelas normas de engenharia de infraestrutura (*anti-pattern* de *data center*). A agregação Top-of-Rack (ToR) e isolamento lógico via VLAN 20 atendem plenamente à segurança e ao desempenho.

### Alternative 3: Firewall Baseado em Software Virtualizado (pfSense em VM)
- **Pros**: Custo de licenciamento zero.
- **Cons**: Cria dependência da disponibilidade do hipervisor dos servidores antes mesmo da conectividade L3 da rede estar operacional.
- **Why not**: O escopo do projeto prioriza *appliances* físicos dedicados de telecomunicações no rack central.

## Consequences

### Positive
- Inspeção profunda de conexões e filtragem de camada 4/7 desacoplada do roteador de agregação.
- Gestão centralizada de escopos, concessões e reservas de endereçamento IP no servidor DHCP com logs de auditoria independentes.
- Eliminação do risco de ACLs locais no roteador bloquearem inadvertidamente pacotes de descoberta DHCP.
- Facilidade de expansão futura para implementação de túneis VPN IPsec e SSL Clientless para acesso remoto dos pesquisadores externos.

### Negative
- Adição de uma nova sub-rede de trânsito (`10.0.1.0/30`) e necessidade de parametrização de tabelas de rotas estáticas bidirecionais no ASA, roteador de borda e roteador interno.
- Inclusão do item físico Cisco ASA 5506-X no orçamento e no espaço físico do Rack 42U.

### Risks
- **Risco**: Assimetria de tráfego ou descarte de pacotes pelo ASA devido à disparidade de níveis de segurança (*security levels*).
- **Mitigação**: Definição rigorosa de rotas estáticas `route inside` e `route outside` e inspeção modular de tráfego ICMP e HTTP em política global (`global_policy`).
