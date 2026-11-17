# Roteiro de Testes e Comandos de Validação do NextGIS Web

Este roteiro apresenta os comandos de terminal passo a passo para validar a integridade, conectividade e correto funcionamento do ecossistema NextGIS Web.

---

## 1. Verificação do Estado dos Contêineres

Execute no terminal do servidor para certificar que todos os microsserviços estão ativos e saudáveis:

```bash
docker compose ps
```

* **Critério de Aceitação**: Todos os 4 contêineres (`ngw_core`, `ngw_postgis`, `ngw_redis`, `ngw_proxy`) devem apresentar o status `Up` sem reinicializações constantes (*restarting*).

---

## 2. Teste de Conectividade com o Banco PostGIS

Teste a comunicação interna com a instância do PostgreSQL e certifique a disponibilidade das funções geoespaciais do PostGIS:

```bash
# Executa consulta da versao do PostgreSQL e do PostGIS via linha de comando
docker compose exec postgis_db psql -U nextgis_admin -d nextgisweb_db -c "SELECT postgis_full_version();"
```

* **Critério de Aceitação**: A saída deve retornar a versão do PostGIS (ex.: `POSTGIS="3.4.x" GEOS="3.12.x" PROJ="9.3.x"`), confirmando que a extensão espacial está carregada e operacional.

---

## 3. Teste de Comunicação com a Fila de Cache Redis

Envie um sinal de ping para o contêiner do Redis:

```bash
docker compose exec redis_cache redis-cli ping
```

* **Critério de Aceitação**: O retorno deve ser exatamente a string `PONG`.

---

## 4. Teste de Resposta da Camada Web (HTTP/HTTPS)

Verifique o código de status retornado pelo proxy Nginx e pelo núcleo da aplicação:

```bash
# Teste de requisicao HTTP local
curl -I http://localhost
```

* **Critério de Aceitação**: O servidor deve responder com o código `HTTP/1.1 200 OK` ou redirecionamento válido `HTTP/1.1 302 Found`, exibindo os cabeçalhos de resposta gerados pelo Nginx.

---

## 5. Teste da API REST e Catálogo de Recursos OGC

Consulte os metadados da aplicação via interface de programação REST:

```bash
# Consulta a versao e informacoes do sistema NextGIS Web
curl -s http://localhost/api/component/pyramid/pkg_version | jq .
```

* **Critério de Aceitação**: Resposta em formato JSON informando a versão do software e os módulos instalados.

---

## 6. Teste de Integridade de Volumes e Persistência

Simule uma parada controlada e subida para atestar que os dados não são perdidos:

```bash
# Parada dos servicos
docker compose down

# Reinicializacao
docker compose up -d

# Validacao de persistencia das tabelas
docker compose exec postgis_db psql -U nextgis_admin -d nextgisweb_db -c "\dt"
```
