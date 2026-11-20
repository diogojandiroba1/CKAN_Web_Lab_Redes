#!/usr/bin/env python3
import json
import os
import re
import sys
import requests

CKAN_URL = os.environ.get("CKAN_URL", "http://localhost")
API_BASE = f"{CKAN_URL}/api/3/action"

def get_token():
    raw = os.environ.get("CKAN_TOKEN", "")
    token_path = os.path.expanduser("~/ckan_api_token.txt")
    if os.path.exists(token_path):
        with open(token_path, "r", encoding="utf-8") as f:
            raw = f.read()
    
    match = re.search(r'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)', raw)
    if match:
        return match.group(1).strip()
    return raw.strip()

def main():
    token = get_token()
    if not token:
        print("[ERRO] Token do CKAN não encontrado!")
        sys.exit(1)

    headers = {
        "Authorization": token,
        "X-CKAN-API-Key": token
    }

    print(f"[*] Conectando à API do CKAN em {API_BASE}...")
    
    # 1. Testar status
    res = requests.get(f"{API_BASE}/status_show", headers=headers)
    if res.status_code != 200:
        print(f"[ERRO] Falha ao consultar status: {res.status_code} - {res.text}")
        sys.exit(1)
    print("[OK] CKAN API operacional.")

    # 2. Criar Organização Oficial do Grupo de Pesquisa da UFS
    org_name = "modelagem-hidrologica-ufs"
    org_data = {
        "name": org_name,
        "title": "Modelagem Hidrológica em Bacias Hidrográficas Nordestinas",
        "description": "Grupo de Pesquisa da Universidade Federal de Sergipe (UFS) liderado pelo Prof. Dr. Alcigeimes Batista Celeste (DEC/CCET). Atua nas linhas de Planejamento e Gerenciamento de Sistemas de Recursos Hídricos e Avaliação dos Impactos sobre Drenagem Urbana e Esgotamento Sanitário. Integra os laboratórios LAMEC/PROEC-UFS, SAMA/DEC-UFS e LabHid/DEC-UFS em cooperação técnica com IFS, UCS, USP, UFCG e Embrapa.",
    }
    res = requests.post(f"{API_BASE}/organization_create", json=org_data, headers=headers)
    if res.status_code == 200:
        print(f"[OK] Organização '{org_data['name']}' criada com sucesso.")
    elif "already exists" in res.text or "Group name already exists" in res.text:
        print(f"[*] Organização '{org_data['name']}' já existe. Atualizando metadados...")
        requests.post(f"{API_BASE}/organization_update", json=org_data, headers=headers)
    else:
        print(f"[WARN] Organização: {res.status_code} - {res.text}")

    # 3. Criar Grupos Temáticos baseados nas Linhas de Pesquisa Oficiais
    groups = [
        {
            "name": "planejamento-recursos-hidricos",
            "title": "Planejamento e Gerenciamento de Recursos Hídricos",
            "description": "Pesquisas voltadas ao dimensionamento e operação de reservatórios com incorporação de estocasticidade, otimização de regras operacionais e avaliação do comportamento de séries hidrológicas em bacias sergipanas (Projetos PEB9697-2020, PVB184-2012, PVB4495-2016)."
        },
        {
            "name": "drenagem-esgotamento-sanitario",
            "title": "Drenagem Urbana e Esgotamento Sanitário",
            "description": "Avaliação dos impactos causados pelos resíduos sólidos e pelas práticas antrópicas sobre os sistemas de drenagem urbana e de esgotamento sanitário no semiárido e litoral nordestino."
        },
        {
            "name": "bacias-hidrograficas-sergipe",
            "title": "Bacias Hidrográficas Sergipanas",
            "description": "Estudos físicos e hidrológicos aplicados às bacias hidrográficas de Sergipe (Rio Sergipe, Rio Jacarecica e afluentes), subsidiando a análise de cheias, inundações e disponibilidade hídrica (Projetos PIB9602-2020, PVB4495-2016)."
        }
    ]

    for g in groups:
        res = requests.post(f"{API_BASE}/group_create", json=g, headers=headers)
        if res.status_code == 200:
            print(f"[OK] Grupo '{g['name']}' criado com sucesso.")
        elif "already exists" in res.text:
            print(f"[*] Grupo '{g['name']}' já existe. Atualizando metadados...")
            requests.post(f"{API_BASE}/group_update", json=g, headers=headers)
        else:
            print(f"[WARN] Grupo {g['name']}: {res.status_code} - {res.text}")

    # 4. Criar Dataset Vinculado aos Projetos Reais (PVB4495-2016 e PIB9602-2020)
    dataset_name = "series-hidrologicas-bacias-sergipanas"
    pkg_data = {
        "name": dataset_name,
        "title": "Séries Hidrológicas em Bacias Hidrográficas Sergipanas (Projeto PVB4495-2016)",
        "owner_org": org_name,
        "notes": "Série histórica diária de monitoramento hidrológico contendo medições de precipitação pluviométrica diária, vazão fluviométrica estimada, cotas de régua e parâmetros físico-químicos (pH, turbidez e oxigênio dissolvido) nas estações de monitoramento das bacias sergipanas (Aracaju, Maruim, Laranjeiras, Riachuelo e Nossa Senhora das Dores). Conjunto de dados estruturado pelo Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (UFS), sob liderança do Prof. Dr. Alcigeimes Batista Celeste, integrando os laboratórios LAMEC, SAMA e LabHid.",
        "groups": [
            {"name": "planejamento-recursos-hidricos"},
            {"name": "bacias-hidrograficas-sergipe"}
        ],
        "tags": [
            {"name": "ufs"},
            {"name": "modelagem-hidrologica"},
            {"name": "recursos-hidricos"},
            {"name": "bacias-sergipanas"},
            {"name": "rio-sergipe"},
            {"name": "pluviometria"},
            {"name": "vazao"}
        ]
    }

    res = requests.post(f"{API_BASE}/package_create", json=pkg_data, headers=headers)
    if res.status_code == 200:
        print(f"[OK] Dataset '{dataset_name}' criado com sucesso.")
    elif "already exists" in res.text or "That name is already in use" in res.text:
        print(f"[*] Dataset '{dataset_name}' já existe. Atualizando metadados...")
        requests.post(f"{API_BASE}/package_update", json=pkg_data, headers=headers)
    else:
        print(f"[WARN] Dataset: {res.status_code} - {res.text}")

    # 5. Fazer upload do arquivo CSV como recurso
    csv_candidates = [
        os.path.join(os.path.dirname(__file__), "dados", "pluviometria_rio_sergipe.csv"),
        os.path.expanduser("~/pluviometria_rio_sergipe.csv"),
        "dados/pluviometria_rio_sergipe.csv",
        "iac/dados/pluviometria_rio_sergipe.csv"
    ]
    csv_file = None
    for cand in csv_candidates:
        if os.path.exists(cand):
            csv_file = cand
            break

    if not csv_file:
        print("[ERRO] Arquivo CSV de hidrologia não encontrado para upload.")
        sys.exit(1)

    print(f"[*] Fazendo upload do recurso CSV: {csv_file}...")
    resource_data = {
        "package_id": dataset_name,
        "name": "Série Diária de Monitoramento Fluviométrico e Qualidade da Água (CSV)",
        "description": "Tabela com 1.830 medições diárias consolidadas de cota (cm), vazão (m³/s), precipitação acumulada (mm) e índices de qualidade das 5 estações monitoradas na Bacia do Rio Sergipe (2024–2026).",
        "format": "CSV"
    }

    with open(csv_file, "rb") as f:
        files = {
            "upload": (os.path.basename(csv_file), f, "text/csv")
        }
        res = requests.post(
            f"{API_BASE}/resource_create",
            data=resource_data,
            files=files,
            headers={"Authorization": token, "X-CKAN-API-Key": token}
        )

    if res.status_code == 200:
        res_json = res.json()
        res_id = res_json.get("result", {}).get("id")
        print(f"[OK] Recurso cadastrado com sucesso! ID: {res_id}")
    else:
        print(f"[WARN] Upload do recurso: {res.status_code} - {res.text}")

    print("\n=== Banco do CKAN atualizado com os dados oficiais do SIGAA/UFS! ===")

if __name__ == "__main__":
    main()
