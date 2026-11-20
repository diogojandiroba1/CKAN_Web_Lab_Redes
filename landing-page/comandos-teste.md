# Roteiro de Testes e Comandos de Validação — CKAN 2.10

Este roteiro documenta os comandos de terminal para testes de integridade, disponibilidade e conformidade da API REST do CKAN, vinculados aos dados oficiais do **Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (UFS)**.

---

## 1. Verificação do Estado dos Contêineres

Execute no terminal do host Ubuntu para verificar os serviços da pilha:

```bash
docker compose ps
```

* **Critério de Aceitação**: Todos os contêineres (`ckan_app`, `ckan_solr`, `ckan_db`, `ckan_redis`, `ckan_datapusher`, `ckan_nginx`) devem apresentar status `Up` ou `Up (healthy)`.

---

## 2. Teste do Mecanismo de Busca Textual (Apache Solr 9)

Valide a integridade do motor de indexação Apache Solr 9:

```bash
docker exec ckan-docker-solr-1 curl -s "http://localhost:8983/solr/ckan/admin/ping" | grep "OK"
```

* **Critério de Aceitação**: Retorno contendo `"status":"OK"`.

---

## 3. Teste da Fila em Memória e Cache (Redis)

Envie uma requisição ping ao serviço Redis:

```bash
docker exec ckan-docker-redis-1 redis-cli ping
```

* **Critério de Aceitação**: Retorno `PONG`.

---

## 4. Teste de Borda HTTP (Nginx)

Consulte a resposta de cabeçalhos HTTP na porta 80 do servidor:

```bash
# Teste local no servidor
curl -I http://localhost/

# Teste externo na instancia AWS
curl -I http://52.54.246.181/
```

* **Critério de Aceitação**: Retorno de código `HTTP/1.1 200 OK` com cabeçalho de proteção `X-Frame-Options: SAMEORIGIN` e cookie de sessão `ckan`.

---

## 5. Testes da API REST com os Dados Oficiais da UFS

### A. Consulta da Organização Oficial do Grupo
```bash
curl -s http://52.54.246.181/api/3/action/organization_show?id=modelagem-hidrologica-ufs | jq '.result.title'
```
* **Critério de Aceitação**: Retorno da string `"Modelagem Hidrológica em Bacias Hidrográficas Nordestinas"`.

### B. Consulta de Grupos Vinculados às Linhas de Pesquisa
```bash
curl -s http://52.54.246.181/api/3/action/group_list | jq .
```
* **Critério de Aceitação**: Presença de `planejamento-recursos-hidricos`, `drenagem-esgotamento-sanitario` e `bacias-hidrograficas-sergipe`.

### C. Busca Textual via Solr pelo Projeto de Pesquisa
```bash
curl -s "http://52.54.246.181/api/3/action/package_search?q=PVB4495" | jq '.result.count'
```
* **Critério de Aceitação**: Retorno de contagem `1` referente ao conjunto *Séries Hidrológicas em Bacias Hidrográficas Sergipanas (Projeto PVB4495-2016)*.

### D. Consulta Tabular no DataStore via API
```bash
curl -s "http://52.54.246.181/api/3/action/datastore_search?resource_id=7d9a72c9-f087-46d0-82ae-1934c1a52958&limit=3" | jq '.result.records'
```
* **Critério de Aceitação**: Array JSON com os registros contendo medições reais de precipitação, cotas fluviométricas e vazões das estações do Rio Sergipe.

---

## 6. Teste de Persistência de Dados e Recuperação

Simule a parada e reinicialização dos contêineres para atestar a persistência nos volumes SSD:

```bash
# Interrupcao controlada
docker compose down

# Reativacao
docker compose up -d

# Validacao da integridade dos metadados
curl -s "http://localhost/api/3/action/package_show?id=series-hidrologicas-bacias-sergipanas" | jq '.success'
```

* **Critério de Aceitação**: Retorno exato `"success": true`.
