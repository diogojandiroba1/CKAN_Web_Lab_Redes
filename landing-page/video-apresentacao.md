# Roteiro de Gravação do Vídeo Demonstrativo — CKAN 2.10

> **Disciplina**: Projeto de Redes de Computadores (Turma 2026.2)  
> **Aluno / Responsável**: Diogo Santos Pires Jandiroba (`diogojandiroba@academico.ufs.br`)  
> **Software Demonstrado**: CKAN 2.10 (*Comprehensive Knowledge Archive Network*)  
> **Grupo de Pesquisa Beneficiado**: Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (UFS)  
> **Líder do Grupo**: Prof. Dr. Alcigeimes Batista Celeste  
> **Laboratórios**: LAMEC/PROEC-UFS, SAMA/DEC-UFS e LabHid/DEC-UFS  
> **Instância em Produção (AWS)**: `http://52.54.246.181/`  
> **Link do Vídeo**: `[Adicionar Link do Vídeo Aqui - YouTube / Google Drive / Loom]`

---

## Roteiro Passo a Passo de Gravação (Duração Alvo: 3 a 5 minutos)

### 1. Abertura e Contextualização do Projeto (00:00 – 00:45)
* **O que falar**:
  * Apresentação pessoal (nome, curso de Engenharia/Ciência da Computação na UFS, disciplina de Projeto de Redes de Computadores);
  * Contexto real do cliente: o projeto de infraestrutura de redes atende à demanda do **Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas**, liderado pelo Prof. Dr. Alcigeimes Batista Celeste (DEC/CCET);
  * Motivação técnica: o grupo opera projetos de pesquisa reais (como o PVB4495-2016 de séries hidrológicas em bacias sergipanas e o PIB9602-2020 na bacia do Rio Jacarecica) e necessitava de um repositório centralizado de dados abertos para consolidar medições pluviométricas e fluviométricas entre os laboratórios LAMEC, SAMA e LabHid, permitindo consumo programático por modelos computacionais.

### 2. Infraestrutura e Topologia de Contêineres (00:45 – 01:45)
* **O que mostrar na tela**:
  * Terminal conectado via SSH na instância AWS EC2 (`ubuntu@52.54.246.181`);
  * Executar `docker compose ps` e explicar a arquitetura desacoplada:
    * `ckan_nginx`: Proxy reverso terminando as conexões HTTP (porta 80) e HTTPS (porta 443);
    * `ckan_app`: Núcleo da plataforma CKAN 2.10 em Python/Flask;
    * `ckan_solr`: Motor Apache Solr 9 para busca textual distribuída e filtros facetados;
    * `ckan_db`: PostgreSQL 15 com extensão PostGIS;
    * `ckan_redis`: Cache em memória e controle de sessões;
    * `ckan_datapusher`: Pipeline assíncrono para conversão de CSVs para o DataStore.
  * Destacar que o servidor opera isolado na VLAN 20 de DMZ do projeto lógico de redes.

### 3. Navegação Prática na Interface Web do CKAN (01:45 – 03:30)
* **O que mostrar no navegador (`http://52.54.246.181/`)**:
  * Abrir a página inicial do portal de dados abertos;
  * Navegar na aba **Organizações**: mostrar a organização oficial cadastrada: *Modelagem Hidrológica em Bacias Hidrográficas Nordestinas*, destacando a vinculação aos laboratórios LAMEC, SAMA e LabHid;
  * Navegar na aba **Grupos**: mostrar os 3 grupos temáticos oficiais:
    1. *Planejamento e Gerenciamento de Recursos Hídricos*;
    2. *Drenagem Urbana e Esgotamento Sanitário*;
    3. *Bacias Hidrográficas Sergipanas*.
  * Abrir o conjunto de dados principal: *Séries Hidrológicas em Bacias Hidrográficas Sergipanas (Projeto PVB4495-2016)*;
  * Clicar no recurso CSV: demonstrar a visualização tabular interativa gerada pelo DataStore com os 1.830 registros de dados diários de cotas, vazões e qualidade da água das 5 estações do Rio Sergipe;
  * Demonstrar a busca instantânea digitando "Jacarecica" ou "Sergipe" na barra de pesquisa.

### 4. Demonstração da API REST via Terminal (03:30 – 04:30)
* **O que falar e executar no terminal**:
  * Executar a consulta direta na API REST:
    ```bash
    curl -s "http://52.54.246.181/api/3/action/package_show?id=series-hidrologicas-bacias-sergipanas" | jq '.result.title'
    ```
  * Executar consulta de dados no DataStore:
    ```bash
    curl -s "http://52.54.246.181/api/3/action/datastore_search?resource_id=7d9a72c9-f087-46d0-82ae-1934c1a52958&limit=3" | jq '.result.records'
    ```
  * Explicar que essa API permite que alunos e pesquisadores integrem diretamente seus scripts de simulação e modelos matemáticos em Python/R aos dados armazenados no servidor da UFS.

### 5. Conclusão Técnica (04:30 – 05:00)
* **O que falar**:
  * Resumir os ganhos: padronização internacional de dados científicos (DCAT), independência de software proprietário com custo zero de licenciamento, alta disponibilidade, integração fluida com as regras de firewall e VLANs projetadas para o laboratório na UFS.
