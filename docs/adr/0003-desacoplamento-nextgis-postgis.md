# ADR-0003: Desacoplamento em Duas Camadas da Plataforma NextGIS Web e PostGIS

**Date**: 2026-11-10  
**Status**: accepted  
**Deciders**: Diogo Santos Pires Jandiroba (Lead Solutions Architect)  

## Context

O grupo de pesquisa em Modelagem Hidrológica manipula bases de dados geoespaciais volumosas, incluindo modelos digitais de elevação (DEM/MDT), malhas vetoriais de redes de drenagem, arquivos raster de sensoriamento remoto e shapefiles de bacias hidrográficas. Processar requisições web HTTP/WMS em concorrência com operações espaciais pesadas (tais como junções espaciais, interseções e consultas PostGIS complexas) em um mesmo ambiente sobrecarregaria os recursos computacionais (CPU e I/O de disco), degradando a experiência dos pesquisadores. Além disso, o documento de levantamento de requisitos formal (`T1 Análise de requisitos.pdf`) estabeleceu a necessidade de 2 servidores dedicados.

## Decision

Desacoplar a infraestrutura de software em duas camadas lógicas e servidores dedicados (executando contêineres Docker independentes):
1. **Servidor 1 (Servidor de Aplicação Web - NextGIS Web)**: Hospeda o servidor web NextGIS Web, proxy reverso Nginx para terminação de requisições e cache estático, além de processadores de fila assíncrona.
2. **Servidor 2 (Servidor de Dados Geoespaciais e Persistência - PostGIS)**: Hospeda o Sistema Gerenciador de Banco de Dados Relacional PostgreSQL compilado com a extensão espacial PostGIS, gerenciando volumes montados em SSD/NVMe dedicados ao repositório de dados cartográficos e rotinas programadas de backup.

## Alternatives Considered

### Alternativa 1: Arquitetura Monolítica All-in-One em Servidor Único
- **Pros**: Reduz a complexidade de configuração de rede entre contêineres; dispensa conexão de rede externa entre backend e banco.
- **Cons**: Competição severa por memória RAM e I/O de disco entre o Nginx/Python e o PostGIS; um travamento ou vazamento de memória da aplicação derruba a integridade do banco de dados.
- **Why not**: Contraria diretamente a especificação do edital e as respostas submetidas no formulário `T1 Análise de requisitos.pdf`, que fixou 2 servidores virtuais/físicos.

### Alternativa 2: Cluster Distribuído Multi-Nó de Alta Disponibilidade (Swarm / Kubernetes)
- **Pros**: Tolerância a falhas automática e balanceamento de carga elástico entre múltiplos nós.
- **Cons**: Complexidade operacional excessiva para o porte do laboratório acadêmico; custos elevados de infraestrutura e sobrecarga desnecessária de orquestração.
- **Why not**: Incompatível com o escopo e o tempo de entrega da disciplina de graduação.

## Consequences

### Positivas
- Isolamento de falhas: instabilidades ou picos de carga na camada web não corrompem nem travam o serviço de armazenamento relacional espacial.
- Dimensionamento proporcional: o Servidor de Dados pode receber maior alocação de memória RAM e storage de alta velocidade, enquanto o Servidor Web prioriza threads de processamento.
- Segurança aprimorada: o banco de dados PostGIS fica restrito à comunicação interna com o Servidor de Aplicação, sem exposição direta de portas públicas para a Internet.

### Negativas
- Introduz tráfego de rede inter-servidor na VLAN 20 para cada transação e consulta espacial.

### Riscos
- **Risco**: Latência de rede entre a camada de aplicação e a camada de dados no processamento de requisições analíticas massivas.
- **Mitigação**: Conexão dos dois servidores físicos/virtuais no mesmo switch com portas Gigabit Ethernet dedicadas e baixa latência (< 1 ms).
