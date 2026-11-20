# Estado do Projeto - Infraestrutura de Redes UFS

**Última Atualização**: 2026-11-20  
**Responsável Técnico**: Diogo Santos Pires Jandiroba (`diogojandiroba@academico.ufs.br`)  
**Cliente / Beneficiário**: Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (UFS)  
**Líder do Grupo**: Prof. Dr. Alcigeimes Batista Celeste (DEC/CCET)  
**Laboratórios Integrados**: LAMEC/PROEC-UFS, SAMA/DEC-UFS e LabHid/DEC-UFS  
**Status Geral**: Migração e Homologação do CKAN 2.10 Concluídas na AWS EC2 (`http://52.54.246.181/`)

---

## 1. Feito (Entregas e Ajustes Concluídos)

- [x] **Substituição e Homologação do Serviço de Software Livre (CKAN 2.10)**:
  - Migração de NextGIS Web para o **CKAN 2.10** (*Comprehensive Knowledge Archive Network*);
  - Pilha de 6 microsserviços conteinerizada e operando com *healthchecks* na instância AWS EC2 (`http://52.54.246.181/`):
    * `ckan_nginx`: Proxy reverso terminando HTTP (porta 80) e HTTPS (porta 443/8443) com limite de *payload* de 100 MB;
    * `ckan_app`: Núcleo da plataforma em Python/Flask conectado ao Apache Solr 9 e PostgreSQL;
    * `ckan_solr`: Motor Apache Solr 9 provendo indexação textual distribuída e busca facetada;
    * `ckan_db`: PostgreSQL 15 com extensão PostGIS para metadados e base DataStore;
    * `ckan_redis`: Cache em memória Redis 7.2 e controle de sessões HTTP;
    * `ckan_datapusher`: Pipeline assíncrono para conversão de CSVs para tabelas relacionais do DataStore.

- [x] **Alinhamento Estrito com os Dados Oficiais do SIGAA / UFS**:
  - Organização oficial cadastrada no portal e na API: `modelagem-hidrologica-ufs` (*Modelagem Hidrológica em Bacias Hidrográficas Nordestinas*);
  - Grupos temáticos configurados segundo as linhas de pesquisa reais:
    1. `planejamento-recursos-hidricos`: *Planejamento e Gerenciamento de Recursos Hídricos* (Projetos PEB9697-2020, PVB184-2012, PVB4495-2016);
    2. `drenagem-esgotamento-sanitario`: *Drenagem Urbana e Esgotamento Sanitário*;
    3. `bacias-hidrograficas-sergipe`: *Bacias Hidrográficas Sergipanas* (Projetos PIB9602-2020, PVB4495-2016).
  - Conjunto de dados ativo e indexado: `series-hidrologicas-bacias-sergipanas` (*Séries Hidrológicas em Bacias Hidrográficas Sergipanas - Projeto PVB4495-2016*), contendo 1.830 registros diários de cotas de régua, vazões estimadas, precipitação acumulada e índices de qualidade da água (pH, turbidez, OD) nas 5 estações fluviométricas do Rio Sergipe;
  - Visualizador tabular do DataStore ativo e consultável via API REST (`/api/3/action/datastore_search`).

- [x] **Atualização Completa dos Artefatos de Automação e Documentação Técnica**:
  - `iac/`: `docker-compose.yml`, `nginx.conf`, `manual-implantacao.md` e `dados/pluviometria_rio_sergipe.csv` atualizados e testados;
  - `landing-page/`: `README.md` (Wiki oficial), `manual-ubuntu.md`, `comandos-teste.md` e `video-apresentacao.md` (Roteiro de 3 a 5 min);
  - `docs/`: `projeto-logico.md`, `diagrama-ocupacao-rack.md`, `projeto-fisico.md`, `bom-orcamento.md`, `guia_packet_tracer.md` e `mecanismos-avaliacao.md` atualizados para o nó `SRV-CKAN`;
  - `NextGisWebFinal.xlsx`: Item 2.1 renomeado para *Servidor Web CKAN Portal 1U*, mantendo 100% dos valores unitários, totais e Atas federais do PNCP (Total global inalterado: R$ 274.229,45).

---

## 2. Próximos Passos

1. **Gravação do Vídeo Demonstrativo (3 a 5 minutos)**:
   - Gravar a demonstração prática seguindo o roteiro de [`landing-page/video-apresentacao.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/video-apresentacao.md), exibindo o portal web em `http://52.54.246.181/` e o consumo via API REST.
2. **Publicação na Wiki Oficial da Disciplina**:
   - Assim que o professor liberar o repositório da Wiki da turma (`https://github.com/elan-git/catalogo/wiki`), inserir a página estruturada a partir de [`landing-page/README.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/README.md).
