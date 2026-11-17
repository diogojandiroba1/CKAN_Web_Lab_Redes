# ADR-0001: Adoção de Infraestrutura On-Premise como Especificação Alvo com Validação Funcional em AWS EC2

**Date**: 2026-11-10  
**Status**: accepted  
**Deciders**: Diogo Santos Pires Jandiroba (Lead Solutions Architect)  

## Context

O projeto simula a atuação de um provedor de serviços de rede e infraestrutura de TI contratado para atender ao grupo de pesquisa em *Modelagem Hidrológica em Bacias Hidrográficas Nordestinas* (CCET / UFS). O escopo acadêmico da disciplina exige o planejamento e dimensionamento de um projeto físico de redes, incluindo cabeamento estruturado, infraestrutura de eletrocalhas/eletrodutos, montagem de racks de telecomunicações e orçamento formal de ativos e passivos para os prédios CT-09 e CT-12. No entanto, é necessária a validação prática e funcional da plataforma de software escolhida (NextGIS Web) com orquestração de contêineres e demonstração de treinamento para os usuários.

## Decision

Projetar e documentar formalmente uma infraestrutura física local dedicada (*On-Premise*) com servidores de rack, switches gerenciáveis, roteadores Cisco e cabeamento Cat6 nas salas do campus da UFS, adotando a nuvem pública AWS (instâncias EC2 com Docker Compose) como plataforma de Prova de Conceito (*Proof of Concept* - PoC) e ambiente prático de treinamento e validação funcional.

## Alternatives Considered

### Alternativa 1: Arquitetura Estritamente em Nuvem (Cloud-Only / AWS)
- **Pros**: Elimina aquisição de servidores locais, nobreaks e climatização; escalabilidade elástica sob demanda.
- **Cons**: Não atende às diretrizes pedagógicas da disciplina de Redes de Computadores, que exigem projeto de cabeamento estruturado, certificação física, planta baixa e layout de telecomunicações.
- **Why not**: O escopo do projeto e os editais de referência da UFS/FEST exigem expressamente a especificação de rede local física e cabeamento nas salas 101 (CT-09) e 201 (CT-12).

### Alternativa 2: Implantação 100% em Servidores Físicos Reais em Laboratório
- **Pros**: Correspondência idêntica entre o projeto executivo e o hardware operante.
- **Cons**: Inviabilidade orçamentária e logística de aquisição imediata de servidores de grande porte e licenças durante o período letivo.
- **Why not**: A indisponibilidade de hardware de servidor de alta densidade no laboratório acadêmico impede a execução dos testes práticos em tempo hábil.

## Consequences

### Positivas
- Cumpre rigorosamente todos os critérios de projeto físico (normas ANSI/TIA-568, ISO/IEC 11801) e orçamentários baseados em Atas de Registro de Preços do PNCP.
- Garante a execução real do NextGIS Web em ambiente acessível publicamente via AWS para testes da professora e treinamento do grupo de pesquisa.
- Padroniza a entrega de software através de contêineres Docker reutilizáveis tanto na nuvem quanto em ambiente bare-metal futuro.

### Negativas
- Exige mapeamento duplo de topologia: o plano de endereçamento IP local da UFS (simulado no Cisco Packet Tracer) e as rotas/Security Groups da VPC na AWS.

### Riscos
- **Risco**: Confusão entre as portas públicas da AWS e as portas locais de produção.
- **Mitigação**: Documentação explícita de correspondência de portas e isolamento de redes no Docker Compose.
