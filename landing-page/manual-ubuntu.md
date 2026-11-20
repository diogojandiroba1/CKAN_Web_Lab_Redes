# Manual de Instalação e Operação no Ubuntu Server — CKAN 2.10

Este guia orienta a instalação e as operações diárias da plataforma CKAN no sistema operacional Ubuntu Server (22.04 LTS ou 24.04 LTS) para suporte às pesquisas do **Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (UFS)**.

---

## 1. Instalação Automatizada via Docker Compose

Para inicializar a infraestrutura com seus 6 microsserviços integrados:

```bash
# 1. Acesse o diretório de automação da infraestrutura
cd iac/

# 2. Suba os serviços em segundo plano
docker compose up -d

# 3. Verifique o status de execução e integridade (healthcheck)
docker compose ps
```

---

## 2. Primeiro Acesso e Autenticação

1. Abra o navegador web no endereço da instância:
   * **Instância em Nuvem (AWS EC2)**: `http://52.54.246.181/`
   * **Instância Local / Datacenter**: `http://localhost/` ou IP estático `http://192.168.20.10/`
2. No canto superior direito da página, clique em **Entrar** (*Log in*);
3. Credenciais de administração geradas no provisionamento:
   * **Usuário**: `ckan_admin`
   * **Senha**: `test1234`
4. Recomenda-se a troca imediata de senha no primeiro acesso através das configurações de perfil.

---

## 3. Fluxo de Trabalho do Pesquisador (SIGAA/UFS)

### A. Estrutura da Organização
A organização oficial já encontra-se pré-cadastrada no portal:
* **Identificador**: `modelagem-hidrologica-ufs`
* **Nome**: *Modelagem Hidrológica em Bacias Hidrográficas Nordestinas*
* **Responsável**: Prof. Dr. Alcigeimes Batista Celeste (Líder do Grupo / DEC-CCET)
* **Laboratórios**: LAMEC/PROEC-UFS, SAMA/DEC-UFS e LabHid/DEC-UFS.

### B. Gestão de Grupos Temáticos
Os dados são categorizados nas seguintes taxonomias vinculadas às linhas de pesquisa:
1. `planejamento-recursos-hidricos`: *Planejamento e Gerenciamento de Recursos Hídricos*;
2. `drenagem-esgotamento-sanitario`: *Drenagem Urbana e Esgotamento Sanitário*;
3. `bacias-hidrograficas-sergipe`: *Bacias Hidrográficas Sergipanas*.

### C. Publicação de Datasets e Séries Temporais
1. Na tela principal, acesse a aba **Conjuntos de dados** $\rightarrow$ **Adicionar Conjunto de Dados**;
2. Preencha os campos obrigatórios:
   * **Título**: *Séries Hidrológicas em Bacias Hidrográficas Sergipanas (Projeto PVB4495-2016)*;
   * **Descrição**: Resumo das medições fluviométricas e pluviométricas;
   * **Organização**: Selecione `Modelagem Hidrológica em Bacias Hidrográficas Nordestinas`;
   * **Grupos**: Vincule a `Planejamento e Gerenciamento de Recursos Hídricos` e `Bacias Hidrográficas Sergipanas`;
   * **Tags**: `ufs`, `modelagem-hidrologica`, `recursos-hidricos`, `bacias-sergipanas`, `rio-sergipe`.
3. Avance para **Adicionar Dados**;
4. No campo do recurso:
   * Selecione o arquivo CSV estruturado (`pluviometria_rio_sergipe.csv`);
   * Defina o formato como `CSV`;
   * Nomeie o recurso como *Série Diária de Monitoramento Fluviométrico e Qualidade da Água (CSV)*.
5. Salve o formulário. O *DataPusher* automaticamente processará as 1.830 linhas e ativará a visualização em grade interativa do DataStore.

---

## 4. Consumo de Dados via Python para Modelagem Hidrológica

Pesquisadores podem consumir diretamente os dados em scripts Python sem depender de downloads manuais:

```python
import requests
import pandas as pd

# Endpoint da API DataStore do CKAN na UFS
API_URL = "http://52.54.246.181/api/3/action/datastore_search"

params = {
    "resource_id": "7d9a72c9-f087-46d0-82ae-1934c1a52958",
    "limit": 500
}

response = requests.get(API_URL, params=params).json()

if response.get("success"):
    records = response["result"]["records"]
    df = pd.DataFrame(records)
    print(f"Registros carregados: {len(df)}")
    print(df[["data_medicao", "nome_estacao", "vazao_estimada_m3_s", "cota_fluviometrica_cm"]].head())
```
