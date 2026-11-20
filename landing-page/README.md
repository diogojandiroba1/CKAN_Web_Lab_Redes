# CKAN — Catálogo Institucional de Dados Abertos e Repositório Hidrológico

> **Catálogo de Manuais de Software Livre da Turma (UFS 2026.2)**  
> **Software**: CKAN 2.10 (*Comprehensive Knowledge Archive Network*)  
> **Responsável Técnico**: Diogo Santos Pires Jandiroba (`diogojandiroba@academico.ufs.br`)  
> **Grupo de Pesquisa**: Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (CCET/UFS)  
> **Líder do Grupo**: Prof. Dr. Alcigeimes Batista Celeste  
> **Laboratórios Integrados**: LAMEC/PROEC-UFS, SAMA/DEC-UFS e LabHid/DEC-UFS  
> **Instância em Nuvem Homologada**: `http://52.54.246.181/`

---

## 1. Visão Geral e Contexto Real da Pesquisa

O **CKAN** é o padrão internacional de código aberto para governança, catalogação e distribuição de dados abertos. Adotado por portais governamentais (*dados.gov.br*, *data.gov*) e instituições científicas, ele foi implantado para atender às demandas de infraestrutura do **Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas**, sediado na Universidade Federal de Sergipe (UFS).

O grupo atua no semiárido e litoral nordestino, regiões caracterizadas pela alternância de secas severas e inundações bruscas. As pesquisas exigem a ingestão e o processamento de séries históricas de precipitação, vazão de rios, balanço hídrico de reservatórios e parâmetros físico-químicos de corpos d'água. 

O CKAN resolve o problema da fragmentação de planilhas locais dispersas entre os laboratórios (LAMEC, SAMA e LabHid). A plataforma centraliza os conjuntos de dados em um repositório auditável, com metadados estruturados, busca textual distribuída e uma API REST que alimenta diretamente os modelos hidrológicos desenvolvidos pelos pesquisadores.

---

## 2. Linhas de Pesquisa e Projetos Vinculados (Dados Oficiais SIGAA/UFS)

A estrutura do catálogo reflete diretamente os projetos de pesquisa cadastrados na UFS:

1. **Linha: Planejamento e Gerenciamento de Sistemas de Recursos Hídricos**
   * **PEB9697-2020**: Avaliação de Ferramenta Computacional para Dimensionamento e Operação de Reservatórios Incorporando Estocasticidade e Riscos;
   * **PVB184-2012**: Otimização Estocástica para Derivação de Regras Operacionais de Reservatórios no Estado de Sergipe;
   * **PIB9602-2020**: Estudo das características físicas e hidrológicas da bacia do rio Jacarecica como subsídio para análise de inundações;
   * **PIB9252-2020**: Estudo hidrológico da bacia hidrográfica do rio Grande, afluente à UHE Sobradinho;
   * **PVB4495-2016**: Avaliação de alterações no comportamento das séries hidrológicas em bacias hidrográficas sergipanas e seus impactos sobre a disponibilidade hídrica.

2. **Linha: Avaliação dos Impactos sobre Drenagem Urbana e Esgotamento Sanitário**
   * Análise dos impactos causados pelo aumento da área impermeabilizada, supressão de mata nativa, carga de sedimentos, agroquímicos e resíduos sólidos nos corpos hídricos de Sergipe.

3. **Instituições Parceiras**:
   * Instituto Federal de Sergipe (IFS), Universidade de Caxias do Sul (UCS), Universidade de São Paulo (USP), Universidade Federal de Campina Grande (UFCG) e Empresa Brasileira de Pesquisa Agropecuária (Embrapa).

---

## 3. Arquitetura da Solução

A solução opera de forma desacoplada em contêineres Docker, conectando a camada web de borda aos serviços de persistência e indexação:

```text
[ Pesquisador / Script Python ou R / Navegador Web ]
                        │
                        ▼  (Porta 80 / 443 TCP)
              ┌─────────────────┐
              │   Nginx Proxy   │ (Terminação HTTP, Cache de Assets e Limite de Payload 100M)
              └────────┬────────┘
                       │
                       ▼  (Porta 5000 TCP Interna)
            ┌─────────────────────┐
            │      CKAN Core      │ ◄──────► ┌────────────────┐
            │   (Python / Flask)  │          │   Redis 7.2    │ (Fila de Sessões e Cache)
            └──────────┬──────────┘          └────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
┌────────────────┐ ┌───────┐ ┌───────────────┐
│ PostgreSQL 15  │ │ Solr9 │ │  DataPusher   │
│ + PostGIS      │ │ Index │ │ (Carga Tabular│
│ (Metadados e   │ │ (Busca│ │ no DataStore) │
│  DataStore)    │ │Texto) │ └───────────────┘
└────────────────┘ └───────┘
```

* **Nginx**: Ponto de terminação de tráfego na DMZ (VLAN 20);
* **CKAN Core (2.10)**: Aplicação central de governança, autenticação e rotas da API REST;
* **Apache Solr 9**: Mecanismo de busca textual e filtros facetados em tempo real;
* **PostgreSQL 15 + PostGIS**: Persistência relacional das bases `ckan_default` (metadados) e `datastore` (tabelas de medições);
* **Redis 7.2**: Cache em memória para aceleração de consultas e controle de concorrência;
* **DataPusher**: Agente assíncrono que ingere os arquivos CSV carregados pelos alunos e popula as tabelas relacionais do DataStore.

---

## 4. Benefícios Práticos para a Universidade

1. **Reprodutibilidade Científica**: Séries temporais de vazão e pluviosidade com identificador persistente e metadados padronizados;
2. **Integração Nativamente Automatizada**: *Scripts* Python/R de simulação hidrológica consomem diretamente o *endpoint* `/api/3/action/datastore_search`;
3. **Segurança e Isolamento de Rede**: O portal opera isolado na VLAN 20 de DMZ, garantindo que o banco de dados interno e os ativos de rede não sofram exposição indevida;
4. **Independência Tecnológica**: Custo zero de aquisição de licenças de software, aderente às diretrizes de dados abertos do governo federal.

---

## 5. Navegação e Documentação Rápida

* [Manual de Instalação e Operação no Ubuntu Server](manual-ubuntu.md)
* [Roteiro de Comandos e Testes de Homologação](comandos-teste.md)
* [Roteiro do Vídeo Demonstrativo](video-apresentacao.md)
* [Automação da Infraestrutura (IaC)](../iac/docker-compose.yml)
* [Projeto de Redes e Infraestrutura](../docs/projeto-logico.md)
