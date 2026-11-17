# ADR-0002: Segmentação Lógica em 4 VLANs com Roteamento Inter-VLAN e Borda Cisco

**Date**: 2026-11-10  
**Status**: accepted  
**Deciders**: Diogo Santos Pires Jandiroba (Lead Solutions Architect)  

## Context

A infraestrutura atende a múltiplos perfis de dispositivos e fluxos de tráfego simultâneos nos prédios CT-09 e CT-12: estações de trabalho de pesquisadores executando processamento pesado de modelagem hidrológica, tráfego web/banco de dados do NextGIS Web, conexões sem fio de dispositivos móveis de visitantes e interfaces de gerenciamento crítico de ativos de rede (switches, roteadores, nobreaks e PDUs). Manter todos os dispositivos em um único domínio de broadcast comprometeria a segurança, a conformidade de dados e o desempenho do link.

## Decision

Segmentar a rede corporativa local em 4 Redes Locais Virtuais (*Virtual Local Area Networks* - VLANs) independentes, utilizando o roteador interno Cisco 2911 como concentrador de roteamento inter-VLAN e gateway de sub-redes, com aplicação de Listas de Controle de Acesso (*Access Control Lists* - ACLs) para isolamento, e o roteador Cisco ISR4321 atuando como roteador de borda (*router_border*) e terminação WAN com a rede da UFS:
1. **VLAN 10 (Gerência - 192.168.10.0/24)**: Acesso administrativo SSH/HTTPS restrito a switches, roteadores e interfaces IPMI/iDRAC.
2. **VLAN 20 (Servidores / DMZ - 192.168.20.0/24)**: Hospedagem da aplicação NextGIS Web e banco de dados relacional e espacial PostgreSQL/PostGIS.
3. **VLAN 30 (Estações de Pesquisa - 192.168.30.0/24)**: Desktops dos pesquisadores nos prédios CT-09 (Sala 101) e CT-12 (Sala 201).
4. **VLAN 40 (Rede Sem Fio / Wi-Fi - 192.168.40.0/24)**: Dispositivos móveis e estações convidadas conectadas via Access Points Omada.

## Alternatives Considered

### Alternativa 1: Rede Plana Única (Flat Network /24 sem VLANs)
- **Pros**: Configuração inicial elementar; dispensa roteamento inter-VLAN.
- **Cons**: Domínio de broadcast único gerando ruído de rede; estações de trabalho teriam visibilidade direta às interfaces de gerência dos switches e portas de banco de dados; impossibilidade de aplicar políticas de QoS ou ACLs granulares.
- **Why not**: Viola as diretrizes de segurança da informação e não atende aos requisitos de projeto corporativo solicitados na disciplina.

### Alternativa 2: Segmentação Bipartida (Produção vs Convidados)
- **Pros**: Menos sub-redes para configurar no Packet Tracer.
- **Cons**: Mistura estações de trabalho de usuários finais com os servidores de banco de dados de bacias hidrográficas e as interfaces administrativas dos ativos de rede.
- **Why not**: Não previne movimentação lateral em caso de comprometimento de uma estação de trabalho de estudante/pesquisador.

## Consequences

### Positivas
- Isolamento estrito da camada de gerência e dos servidores de banco de dados através de ACLs stateful/stateless.
- Contenção de tempestades de broadcast (*broadcast storms*) em domínios restritos.
- Facilidade de dimensionamento e aplicação de QoS prioritário para o tráfego geoespacial e dados de modelagem.

### Negativas
- Requer configuração explícita de troncos 802.1Q (*trunking*) em todas as portas de uplink dos switches Cisco 2960-24TT e subinterfaces no roteador Cisco 2911.

### Riscos
- **Risco**: Bloqueio inadvertido de acesso das estações dos pesquisadores (VLAN 30) aos serviços HTTP/WMS do NextGIS (VLAN 20).
- **Mitigação**: Definição criteriosa da matriz de comunicação e testes de validação via Packet Tracer liberando portas 80/443 e bloqueando porta 5432 (PostGIS) para clientes diretos não autorizados.
