# Manual de Implantação e Automação (IaC) — CKAN 2.10

Este guia detalha a implantação da infraestrutura de dados abertos baseada no **CKAN 2.10** (*Comprehensive Knowledge Archive Network*). O arranjo desacopla o catálogo em microsserviços conteinerizados: motor de busca e indexação facetada com **Apache Solr 9**, banco relacional com **PostgreSQL 15 / PostGIS**, fila de sessões em memória com **Redis 7.2**, extrator tabular com **DataPusher** e terminação de tráfego com *proxy reverso* **Nginx**.

---

## 1. Requisitos de Hardware e Sistema Operacional

O ambiente foi homologado sobre **Ubuntu Server 24.04 LTS (x86_64)**, tanto na infraestrutura física do *datacenter* (servidor de borda 1U Dell PowerEdge) quanto em instâncias de nuvem (**AWS EC2 t3.medium** ou superior):

* **CPU**: 2 vCPUs dedicadas (arquitetura x86_64);
* **Memória RAM**: 4 GB no mínimo (recomendado 8 GB para comportar o *heap* da JVM do Solr 9 e a base PostgreSQL simultaneamente);
* **Armazenamento**: 30 GB SSD em partição `/var/lib/docker`;
* **Rede**: Portas TCP 80 (*HTTP*), 443 (*HTTPS*) e 22 (*SSH*) liberadas nas regras de entrada da VLAN de DMZ e *security groups*.

---

## 2. Preparação do Host e Docker Engine

Instale os pacotes oficiais do Docker Engine no nó Ubuntu:

```bash
# 1. Atualizar indice de pacotes
sudo apt update && sudo apt upgrade -y

# 2. Instalar certificados e ferramentas de transporte
sudo apt install -y ca-certificates curl gnupg lsb-release

# 3. Importar a chave GPG do repositorio oficial do Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 4. Configurar repositorio estavel
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Instalar Docker Engine e plugin do Docker Compose
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 6. Conceder permissao de execucao ao usuario local
sudo usermod -aG docker $USER
```

> Reinicie a sessão SSH (`exit` e reconexão) para aplicar as permissões do grupo `docker`.

---

## 3. Topologia dos Arquivos de Automação

O diretório `/iac` centraliza a declaração da pilha:

```text
iac/
├── docker-compose.yml              # Definicao declarativa multicamada dos servicos
├── nginx.conf                      # Proxy reverso, headers de seguranca e limites de payload
├── dados/
│   └── pluviometria_rio_sergipe.csv # Dataset hidrologico de Sergipe (1.830 registros)
└── manual-implantacao.md            # Documentacao de operacao e manutencao
```

---

## 4. Inicialização e Subida dos Contêineres

Para iniciar a pilha completa com orquestração automática de dependências e checagens de integridade (*healthchecks*):

```bash
cd iac/
docker compose up -d
```

### Verificação do Estado da Pilha

```bash
docker compose ps
```

Saída esperada:

```text
NAME              IMAGE                              SERVICE       STATUS                   PORTS
ckan_app          ckan/ckan-base:2.10                ckan          Up 2 minutes (healthy)   5000/tcp
ckan_datapusher   ckan/ckan-base-datapusher:0.0.21   datapusher    Up 2 minutes (healthy)   8800/tcp
ckan_db           postgis/postgis:15-3.3-alpine      db            Up 2 minutes (healthy)   5432/tcp
ckan_nginx        nginx:stable-alpine                nginx_proxy   Up 2 minutes             0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
ckan_redis        redis:7.2-alpine                   redis         Up 2 minutes (healthy)   6379/tcp
ckan_solr         ckan/ckan-solr:2.10-solr9          solr          Up 2 minutes (healthy)   8983/tcp
```

---

## 5. Rotina de Carga do Dataset Hidrológico da UFS (SIGAA)

Para popular a organização do grupo de pesquisa, grupos temáticos e carregar a série histórica de monitoramento da Bacia do Rio Sergipe (Projeto PVB4495-2016):

```bash
# Execucao do script de seed de dados via API REST
python3 seed_ckan_data.py
```

O script autentica via *token* JWT de administrador, cria a organização `modelagem-hidrologica-ufs` (*Modelagem Hidrológica em Bacias Hidrográficas Nordestinas*), vincula os grupos temáticos de recursos hídricos e dispara o *upload* multipart do CSV para o catálogo e o DataStore.

---

## 6. Manutenção e Ciclo de Vida

```bash
# Inspecionar logs unificados em tempo real
docker compose logs -f ckan

# Interromper servicos preservando volumes persistentes
docker compose stop

# Reiniciar servicos
docker compose start

# Destruir contêineres e redes (mantendo volumes)
docker compose down
```
