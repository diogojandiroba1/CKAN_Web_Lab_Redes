# Manual de Implantação e Automação (IaC)

Este documento descreve o procedimento de implantação automatizada da plataforma **NextGIS Web** integrada ao banco relacional e espacial **PostgreSQL 16 com extensão PostGIS 3.4**, fila de mensageria **Redis 7.2** e proxy reverso **Nginx**.

---

## 1. Pré-requisitos de Sistema

O ambiente de execução foi homologado para **Ubuntu Server 24.04 LTS (x86_64)**, tanto em servidores físicos dedicados no datacenter quanto em instâncias de computação em nuvem (**AWS EC2 t3.medium** ou superior).

* **Processador**: 2 vCPUs ou superior;
* **Memória RAM**: Mínimo de 4 GB (recomendado 8 GB para indexação espacial pesada);
* **Armazenamento**: 30 GB SSD (volumes persistentes de dados geográficos e imagens raster);
* **Rede**: Portas TCP 80 (HTTP), 443 (HTTPS) e 22 (SSH) abertas no firewall / grupo de segurança.

---

## 2. Instalação do Docker e Docker Compose

Atualize os pacotes do sistema e instale os componentes oficiais do Docker Engine:

```bash
# 1. Atualizacao dos repositorios locais
sudo apt update && sudo apt upgrade -y

# 2. Instalacao de utilitarios de seguranca e certificados
sudo apt install -y ca-certificates curl gnupg lsb-release

# 3. Adicao da chave GPG oficial do Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 4. Configuracao do repositorio estavel do Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Instalacao dos pacotes Docker Engine e Compose Plugin
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 6. Adicao do usuario atual ao grupo docker (evita uso de sudo)
sudo usermod -aG docker $USER
```

> **Atenção**: Encerre a sessão SSH (`exit`) e reconecte para que a permissão de grupo seja carregada.

---

## 3. Estrutura de Arquivos e Execução

Os arquivos de automação encontram-se organizados neste diretório (`/iac`):

```text
iac/
├── docker-compose.yml   # Orquestracao multicamadas dos servicos
├── nginx.conf           # Proxy reverso e tratamento de cabecalhos
└── manual-implantacao.md # Guia de inicializacao e testes
```

### Inicialização dos Serviços em Segundo Plano

Execute no terminal dentro do diretório `/iac`:

```bash
# Subir contêineres em modo daemon
docker compose up -d
```

### Verificação do Estado da Aplicação

```bash
# Verificar contêineres em execução
docker compose ps
```

Saída esperada:

```text
NAME          IMAGE                      COMMAND                  SERVICE       CREATED          STATUS          PORTS
ngw_core      nextgis/nextgisweb:latest  "/entrypoint.sh run…"    nextgisweb    30 seconds ago   Up 30 seconds   8080/tcp
ngw_postgis   postgis/postgis:16-3.4     "docker-entrypoint.s…"   postgis_db    30 seconds ago   Up 30 seconds   5432/tcp
ngw_proxy     nginx:alpine               "/docker-entrypoint.…"   nginx_proxy   30 seconds ago   Up 30 seconds   0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
ngw_redis     redis:7.2-alpine           "docker-entrypoint.s…"   redis_cache   30 seconds ago   Up 30 seconds   6379/tcp
```

### Inspeção de Logs em Tempo Real

```bash
# Monitorar logs de inicializacao da aplicacao
docker compose logs -f nextgisweb
```

---

## 4. Parada e Manutenção dos Serviços

```bash
# Pausar os serviços sem remover os dados
docker compose stop

# Reiniciar todos os serviços
docker compose restart

# Encerrar os serviços (mantendo os volumes de dados persistentes)
docker compose down
```
