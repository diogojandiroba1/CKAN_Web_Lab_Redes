# ADR-0004: Abstração Canônica de Estações de Trabalho e Modelagem da Topologia Lógica no Cisco Packet Tracer

**Date**: 2026-11-10  
**Status**: accepted  
**Deciders**: Diogo Santos Pires Jandiroba (Lead Solutions Architect)  

## Context

A infraestrutura física da rede corporativa atende a 97 pontos de telecomunicações distribuídos entre o Prédio CT-09 (49 pontos na Sala 101) e o Prédio CT-12 (48 pontos na Sala 201) da Universidade Federal de Sergipe. Representar a totalidade das 97 estações de trabalho de forma exaustiva no ambiente de simulação Cisco Packet Tracer (versão 9.0.1) satura o espaço visual de trabalho (*workspace*), sobrepõe identificadores de portas de rede e gera overhead desnecessário de simulação, sem agregar valor à validação das políticas de roteamento inter-VLAN, comutação L2, troncos 802.1Q, concessão de endereçamento DHCP e listas de controle de acesso (ACLs).

Faz-se necessária a definição de um modelo canônico de abstração no Packet Tracer que simplifique o diagrama visual mantendo a fidelidade das camadas de núcleo (*core*), distribuição, borda de campus, servidores de aplicação e segurança lógica.

## Decision

Adotar uma abstração canônica na modelagem do Cisco Packet Tracer 9.0.1, representando o parque de estações de pesquisa por 2 estações de trabalho (*workstations*) representativas por sala/prédio (`WS-CT12-01` e `WS-CT12-02` no CT-12; `WS-CT09-01` e `WS-CT09-02` no CT-09), 1 estação de gerência administrativa (`WS-ADMIN` com IP estático) e 1 ponto de acesso sem fio (*Access Point*) por sala, preservando a totalidade dos ativos de infraestrutura de rede e servidores:

1. **Roteador de Borda (`router_border` - Cisco ISR 4321)**: Interconexão WAN com o campus UFS via enlace ponto a ponto `200.17.0.0/30` e enlace interno `10.0.0.0/30` com conversão de endereços NAT/PAT.
2. **Roteador Interno (`router_interno` - Cisco 2911)**: Concentrador de roteamento inter-VLAN (*Router-on-a-Stick* via tronco 802.1Q na interface `GigabitEthernet0/0`), servidor DHCP para as VLANs 30 e 40, e aplicador das ACLs estendidas de isolamento.
3. **Switches de Distribuição e Acesso (Cisco Catalyst 2960-24TT)**:
   - `SW-CT12`: Switch central alocado no rack 42U do CT-12 com portas tronco para o roteador interno (`g0/1`) e enlace inter-prédios para o CT-09 (`g0/2`), portas de acesso na VLAN 20 para servidores e portas na VLAN 30/40;
   - `SW-CT09`: Switch de acesso no rack 24U da Sala 101 conectado via tronco óptico simulado (`g0/2`), atendendo às estações locais e AP.
4. **Servidores Dedicados da DMZ (VLAN 20)**: Servidor de aplicação geoespacial NextGIS Web (`SRV-NEXTGIS`, IP 192.168.20.10) e servidor de banco de dados espacial PostgreSQL/PostGIS (`SRV-POSTGIS`, IP 192.168.20.20), ambos em portas de acesso exclusivas.

### Diagrama Textual da Topologia Lógica Canônica

```
                      +-----------------------------+
                      |   Nuvem / Internet / UFS    |
                      |      (200.17.0.1/30)        |
                      +--------------+--------------+
                                     | Cabo Direto (GbE)
                                     v
                      +-----------------------------+
                      |    router_border (ISR4321)  |
                      |   g0/0/1: 200.17.0.2/30     |
                      |   g0/0/0: 10.0.0.1/30 (NAT) |
                      +--------------+--------------+
                                     | Cabo Direto (GbE) - Enlace P2P 10.0.0.0/30
                                     v
                      +-----------------------------+
                      |    router_interno (2911)    |
                      |   g0/1: 10.0.0.2/30         |
                      |   g0/0: Tronco 802.1Q       |
                      |   - g0/0.10: 192.168.10.1   |
                      |   - g0/0.20: 192.168.20.1   |
                      |   - g0/0.30: 192.168.30.1   |
                      |   - g0/0.40: 192.168.40.1   |
                      +--------------+--------------+
                                     | Cabo Direto (Tronco 802.1Q)
                                     v
       ===================== PRÉDIO CT-12 (SALA 201) =====================
                      +-----------------------------+
                      |    SW-CT12 (Cisco 2960)     |
                      |   VLAN 10 SVI: .10.2        |
                      +------+-------+-------+------+
                             |       |       |      |
            +----------------+       |       |      +-----------------+
            | (VLAN 20)              | (VLAN 30)   | (VLAN 40)       | (Tronco 802.1Q)
            v                        v             v                 v (Backbone Óptico)
    [Servidores DMZ]            [Estações CT-12]  [AP CT-12]   [Para SW-CT09]
    - NextGIS Web (.20.10)      - WS-CT12-01 (DHCP) (Wi-Fi)           |
    - PostGIS DB (.20.20)       - WS-CT12-02 (DHCP)                   |
                                - WS-ADMIN (.30.10)                   |
                                                                      v
       ===================== PRÉDIO CT-09 (SALA 101) =====================
                                            +-----------------------------+
                                            |    SW-CT09 (Cisco 2960)     |
                                            |   VLAN 10 SVI: .10.3        |
                                            +--------------+--------------+
                                                           |
                                      +--------------------+--------------------+
                                      | (VLAN 30)                               | (VLAN 40)
                                      v                                         v
                              [Estações CT-09]                              [AP CT-09]
                              - WS-CT09-01 (DHCP)                           (Wi-Fi)
                              - WS-CT09-02 (DHCP)
```

### Matriz de Mapeamento de Portas e Equipamentos no Packet Tracer

| Dispositivo Origem | Porta Origem | Dispositivo Destino | Porta Destino | Meio Físico | Atribuição Lógica / VLAN |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `router_border` | `GigabitEthernet0/0/0` | `router_interno` | `GigabitEthernet0/1` | Cabo Par Trançado Direto | Trânsito P2P (10.0.0.0/30) |
| `router_interno` | `GigabitEthernet0/0` | `SW-CT12` | `GigabitEthernet0/1` | Cabo Par Trançado Direto | Tronco 802.1Q (VLANs 10, 20, 30, 40) |
| `SW-CT12` | `GigabitEthernet0/2` | `SW-CT09` | `GigabitEthernet0/2` | Cabo Par Trançado Direto | Tronco 802.1Q (Backbone Campus) |
| `SW-CT12` | `FastEthernet0/1` | `SRV-NEXTGIS` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 20 (IP 192.168.20.10) |
| `SW-CT12` | `FastEthernet0/2` | `SRV-POSTGIS` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 20 (IP 192.168.20.20) |
| `SW-CT12` | `FastEthernet0/3` | `WS-ADMIN` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 30 (IP 192.168.30.10 estático) |
| `SW-CT12` | `FastEthernet0/4` | `WS-CT12-01` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 30 (Cliente DHCP) |
| `SW-CT12` | `FastEthernet0/5` | `WS-CT12-02` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 30 (Cliente DHCP) |
| `SW-CT12` | `FastEthernet0/6` | `AP-CT12` | `Port 0` | Cabo Par Trançado Direto | Acesso VLAN 40 (SSID Hidro_Pesquisa) |
| `SW-CT09` | `FastEthernet0/1` | `WS-CT09-01` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 30 (Cliente DHCP) |
| `SW-CT09` | `FastEthernet0/2` | `WS-CT09-02` | `FastEthernet0` | Cabo Par Trançado Direto | Acesso VLAN 30 (Cliente DHCP) |
| `SW-CT09` | `FastEthernet0/3` | `AP-CT09` | `Port 0` | Cabo Par Trançado Direto | Acesso VLAN 40 (SSID Hidro_Pesquisa) |

## Alternatives Considered

### Alternative 1: Modelagem Exaustiva de Todas as 97 Estações Físicas
- **Pros**: Correspondência biunívoca numérica entre o número de tomadas RJ-45 da planta física e os ícones do simulador.
- **Cons**: Espaço de trabalho sobrecarregado no Packet Tracer com 97 nós terminais; incapacidade de inspecionar visualmente o tráfego de pacotes (modo simulação PDU); degradação no desempenho gráfico do simulador.
- **Why not**: O objetivo pedagógico e técnico da topologia lógica é validar o roteamento, encapsulamento 802.1Q e ACLs, e não replicar a densidade de portas de patch panel, a qual já se encontra documentada no projeto físico.

### Alternative 2: Modelagem Monoprédio com Apenas 1 Estação e 1 Switch
- **Pros**: Mínima complexidade e montagem mais rápida no simulador.
- **Cons**: Não permite simular o enlace inter-prédios entre CT-09 e CT-12; oculta o comportamento do tronco 802.1Q entre switches de acesso; impede demonstrar a distribuição dinâmica de endereços em diferentes salas via DHCP relay/broadcast L2.
- **Why not**: Descaracterizaria a estrutura de campus da Universidade Federal de Sergipe e suprimiria o teste do backbone entre salas.

### Alternative 3: Simulação Exclusiva de Equipamentos de Infraestrutura sem Estações Finais
- **Pros**: Reduz a topologia aos roteadores e switches.
- **Cons**: Impossibilita a verificação funcional fim a fim de resolução DNS, requisições HTTP na porta 80/443 e bloqueio de porta 5432 nas estações de trabalho através da interface de linha de comando (*CLI*) dos computadores de usuário.
- **Why not**: Impede demonstrar o cumprimento dos requisitos funcionais da aplicação NextGIS aos usuários finais.

## Consequences

### Positive
- Clareza visual e facilidade de depuração didática das conexões durante a apresentação à banca e à professora da disciplina.
- Fidelidade técnica integral de todos os componentes de comutação L2, roteamento L3, segurança por ACLs, endereçamento IP e serviços da DMZ.
- Agilidade na execução de testes de conectividade (*ping*, *traceroute*, requisições HTTP e tentativas de acesso bloqueadas).
- Facilidade de exportação do arquivo `.pkt` e inclusão do diagrama limpo no documento técnico.

### Negative
- Não demonstra a ocupação de portas e o comportamento de tempestade de broadcast sob carga de 97 nós simultâneos no ambiente simulado do Packet Tracer.

### Risks
- **Risco**: Avaliação interpretar a topologia lógica simplificada como subdimensionamento da rede física.
- **Mitigação**: Os Capítulos 4 (Projeto Físico) e 5 (Projeto Detalhado e Orçamento) da documentação especificam de forma pormenorizada a matriz completa de 97 pontos de dados, patch panels de 24 portas, switches de acesso e patch cords, estabelecendo que a topologia lógica em Packet Tracer atua como modelo funcional canônico de validação.
