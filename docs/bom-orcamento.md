# Lista Técnica de Materiais (BOM) e Orçamento PNCP

Este documento consolida a Lista Técnica de Materiais (*Bill of Materials* - BOM) dimensionada para a infraestrutura de redes e tecnologia da informação dos laboratórios nos prédios CT-09 e CT-12 da Universidade Federal de Sergipe (UFS).

O levantamento orçamentário está fundamentado em **Atas de Registro de Preços (ARP) e Pregões Eletrônicos vigentes na Esfera Federal** extraídos do Portal Nacional de Contratações Públicas (PNCP), em estrita conformidade com a Lei nº 14.133/2021.

A planilha executiva correspondente encontra-se na raiz do repositório como [`NextGisWebFinal.xlsx`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal.xlsx), formatada no padrão do TP-Link Omada Designer com as colunas em destaque em **laranja** (*Tipo Dispositivo* e *Ata Vigente / ID de Contratação PNCP*).

---

## 1. Atas e Pregões Federais Selecionados (Pasta `atas/`)

Os itens foram mapeados a partir do acervo de contratações públicas federais:

| Órgão Gerenciador Federal | Processo / Pregão | Número da Ata | ID Contratação PNCP | Categoria Atendida |
| :--- | :--- | :---: | :---: | :--- |
| **AGU** (Advocacia-Geral da União) | PE SRP nº 11/2026 (Proc. 00693.001224/2025-44) | Ata 07/2026 | `26994558008450-1-000011/2026` | Switches, Roteador Gateway, Fibras e Patch Cords |
| **DNIT** (Depto. Nac. Infraestrutura de Transportes) | PE SRP nº 90368/2025 (Proc. 50600.004977/2025-71) | Ata 90368/2025 | `04892707000100-1-000368/2025` | Patch Panels Cat6, Cabos Cat6 Furukawa e Keystones |
| **Polícia Federal** (MJSP - DTI/PF) | PE SRP nº 90004/2026 (Proc. 08206.000245/2024-18) | Atas 05 e 08/2026 | `00394494008030-1-000004/2026` | Servidores Rack 1U/2U, Storage NAS, Rack 42U e PDUs |
| **Embrapa** (Alimentos e Territórios) | PE nº 90003/2025 (Proc. SEI 12539336) | Ata SEI 12741050 | `00348003002598-1-000003/2025` | Nobreak Senoidal Online 3000VA Rack (PHD EA 3K) |
| **UFG** (Universidade Federal de Goiás) | PE SRP nº 90026/2024 (Proc. 23070.011896/2024-18) | Ata SEI 80/2025 | `01567601000143-1-000026/2024` | Ponto de Acesso Corporativo Wi-Fi 6 PoE |
| **ESA / Exército Brasileiro** (Ministério da Defesa) | PE nº 90043/2025 (Proc. 64511.015386/2025-33) | Ata 37/2026 | `09575541000112-1-000043/2025` | Mini-Rack 20U/24U de Piso/Parede (MaxEletron) |
| **Marinha do Brasil** (PAPEM / Comando da Marinha) | PE nº 12/2026 (Proc. 63438.005343/2026-98) | Ata 05/2026 | `00394502043897-1-000012/2026` | Nobreak Senoidal 1500VA para Rack Secundário |
| **CREFONO 6ª Região** | PE nº 17/2026 (Proc. 13/2026) | Ata 01/2026 | `01646861000104-1-000017/2026` | Workstations de Pesquisa e Monitores 27" |

---

## 2. Planilha Orçamentária Consolidada (BOM)

### 2.1 Ativos de Rede e Comunicação (Simulação TP-Link Omada)

![Lista de Ativos e Quantitativos Exportados do TP-Link Omada](img/omada_lista_equipamentos.png)
*Link para o arquivo anexado: [omada_lista_equipamentos.png](img/omada_lista_equipamentos.png)*  
*Link para a planilha executiva formatada (Slide 8): [NextGisWebFinal.xlsx](../NextGisWebFinal.xlsx)*

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte TR |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1.1** | ER7206 | Roteador / Gateway VPN | 26994558008450-1-000011/2026 | Roteador corporativo Multi-Gigabit VPN, Firewall SPI, Dual WAN | TP-Link | 1 | 2.850,00 | 2.850,00 | [PNCP](https://pncp.gov.br) |
| **1.2** | SG2210P | Switch PoE+ Gigabit | 26994558008450-1-000011/2026 | Switch gerenciável 10P GbE com 8 portas PoE+ (61W total) para APs | TP-Link | 2 | 1.420,00 | 2.840,00 | [PNCP](https://pncp.gov.br) |
| **1.3** | SG3428 | Switch 24P Gigabit L2+ | 26994558008450-1-000011/2026 | Switch gerenciável 24 portas Gigabit com 4 slots SFP 1G para agregação | TP-Link | 4 | 2.690,00 | 10.760,00 | [PNCP](https://pncp.gov.br) |
| **1.4** | EAP610 | Access Point Wi-Fi 6 | 01567601000143-1-000026/2024 | Access Point teto dual-band AX1800 Wi-Fi 6 Gigabit PoE (1x CT-09 e 1x CT-12) | TP-Link | 2 | 980,00 | 1.960,00 | [PNCP](https://pncp.gov.br) |
| **1.5** | CAT.6 | Cabo U/UTP Cat6 (m) | 04892707000100-1-000368/2025 | Cabo de par trançado Categoria 6 23 AWG LSZH azul para ramais das bancadas | Furukawa | 24 m | 2,40 | 57,60 | [PNCP](https://pncp.gov.br) |
| **1.6** | SMF | Cabo Óptico Monomodo (m) | 26994558008450-1-000011/2026 | Cabo óptico monomodo 9/125 $\mu$m geleado subterrâneo interligação CT09-CT12 | Furukawa | 31 m | 12,00 | 372,00 | [PNCP](https://pncp.gov.br) |
| **Subtotal** | | | | **Subtotal Seção 1 (Ativos de Rede e Comunicação)** | | | | **18.839,60** | |

> **Nota sobre o Roteador de Borda da Operadora (`ISP-UFS`)**: O equipamento `ISP-UFS` não integra as despesas deste projeto por tratar-se de ativo de telecomunicações preexistente da rede metropolitana da Universidade Federal de Sergipe.

---

### 2.2 Servidores Corporativos e Armazenamento Central (Sistema NextGIS)

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte TR |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **2.1** | -- | Servidor Web NextGIS 1U | 00394494008030-1-000004/2026 | Servidor Rack 1U, Intel Xeon Silver, 64 GB RAM DDR4 ECC, 2x 480 GB SSD NVMe | Dell | 1 | 24.500,00 | 24.500,00 | [PNCP](https://pncp.gov.br) |
| **2.2** | -- | Servidor Banco PostGIS 2U | 00394494008030-1-000004/2026 | Servidor Rack 2U, Intel Xeon Silver, 128 GB RAM DDR4 ECC, 4x 1.2 TB SAS 10K RAID 10 | Dell | 1 | 38.900,00 | 38.900,00 | [PNCP](https://pncp.gov.br) |
| **2.3** | -- | Servidor DHCP Dedicado 1U | 00394494008030-1-000004/2026 | Servidor Rack 1U, Intel Xeon E-2324, 32 GB RAM DDR4 ECC, 2x 240 GB SSD SATA | Dell | 1 | 16.800,00 | 16.800,00 | [PNCP](https://pncp.gov.br) |
| **2.4** | -- | Storage NAS Backup 4B | 00394494008030-1-000004/2026 | Unidade NAS 4 Baias 16 TB brutos RAID 5 para repositório de cópias de segurança | QNAP | 1 | 9.500,00 | 9.500,00 | [PNCP](https://pncp.gov.br) |
| **Subtotal** | | | | **Subtotal Seção 2 (Servidores e Armazenamento Central)** | | | | **89.700,00** | |

---

### 2.3 Gabinetes, Passivos e Cabeamento Estruturado

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte TR |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **3.1** | -- | Rack Fechado 42U (CT-09) | 00394494008030-1-000004/2026 | Rack fechado 19" 42U x 1000 mm com porta de vidro temperado e exaustão (CT-09) | MaxEletron | 1 | 4.800,00 | 4.800,00 | [PNCP](https://pncp.gov.br) |
| **3.2** | -- | Mini-Rack 24U (CT-12) | 09575541000112-1-000043/2025 | Gabinete padrão 19" 24U x 670 mm de piso/parede soldado para 400 kg | MaxEletron | 1 | 1.189,00 | 1.189,00 | [PNCP](https://pncp.gov.br) |
| **3.3** | -- | Patch Panel Cat6 24P | 04892707000100-1-000368/2025 | Painel de manobra 24 portas RJ-45 Cat6 T568A/B Multilan Furukawa | Furukawa | 5 | 110,57 | 552,85 | [PNCP](https://pncp.gov.br) |
| **3.4** | -- | Caixa Cabo Cat6 305m | 04892707000100-1-000368/2025 | Caixa com 305 m cabo U/UTP Cat6 23 AWG 4 pares capa LSZH azul (R$ 2,40/m) | Furukawa | 8 | 732,00 | 5.856,00 | [PNCP](https://pncp.gov.br) |
| **3.5** | -- | Conector Keystone Cat6 | 04892707000100-1-000368/2025 | Módulo conector fêmea Keystone RJ-45 Cat6 SohoPlus para espelhos | Furukawa | 120 | 18,50 | 2.220,00 | [PNCP](https://pncp.gov.br) |
| **3.6** | -- | Patch Cord Cat6 1,5m | 26994558008450-1-000011/2026 | Cabo manobra Cat6 1,5 m conectorizado de fábrica LSZH azul T568A | Furukawa | 100 | 14,00 | 1.400,00 | [PNCP](https://pncp.gov.br) |
| **3.7** | -- | Patch Cord Cat6 2,5m | 26994558008450-1-000011/2026 | Cabo manobra Cat6 2,5 m conectorizado de fábrica LSZH azul T568A | Furukawa | 30 | 18,00 | 540,00 | [PNCP](https://pncp.gov.br) |
| **3.8** | -- | Guia de Cabos 1U | 00394494008030-1-000004/2026 | Organizador horizontal de cabos 1U fechado metálico padrão 19" | Furukawa | 6 | 55,00 | 330,00 | [PNCP](https://pncp.gov.br) |
| **3.9** | -- | Régua PDU 12 Tomadas | 00394494008030-1-000004/2026 | Calha PDU 12 tomadas 20A NBR 14136 com disjuntor bipolar para rack | APC / SMS | 3 | 260,00 | 780,00 | [PNCP](https://pncp.gov.br) |
| **3.10** | -- | DIO Óptico 1U 24F | 26994558008450-1-000011/2026 | Distribuidor Interno Óptico 1U 24 fibras com acopladores LC-UPC | Furukawa | 2 | 720,00 | 1.440,00 | [PNCP](https://pncp.gov.br) |
| **3.11** | -- | Nobreak Senoidal 3kVA | 00348003002598-1-000003/2025 | Nobreak senoidal online dupla conversão 3000 VA / 2700 W padrão rack 2U (PHD EA 3K) | PHD / SMS | 1 | 4.997,00 | 4.997,00 | [PNCP](https://pncp.gov.br) |
| **3.12** | -- | Nobreak Senoidal 1.5kVA | 00394502043897-1-000012/2026 | Nobreak senoidal interativo 1500 VA para rack secundário (CT-12) | TS Shara | 1 | 1.450,00 | 1.450,00 | [PNCP](https://pncp.gov.br) |
| **Subtotal** | | | | **Subtotal Seção 3 (Passivos e Infraestrutura)** | | | | **25.554,85** | |

---

### 2.4 Estações de Trabalho e Periféricos de Pesquisa

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte TR |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **4.1** | -- | Workstation Modelagem | 01646861000104-1-000017/2026 | Estação de trabalho Core i7, 32 GB RAM, SSD 1 TB NVMe, GPU RTX 4060 para SIG | NEP / Dell | 15 | 6.999,00 | 104.985,00 | [PNCP](https://pncp.gov.br) |
| **4.2** | -- | Monitor 27" QHD IPS | 01646861000104-1-000017/2026 | Monitor profissional 27 polegadas IPS QHD (2560x1440) com ajuste de altura | Dell / NEP | 15 | 1.850,00 | 27.750,00 | [PNCP](https://pncp.gov.br) |
| **4.3** | -- | Multifuncional Laser A3/A4 | 26994558008450-1-000011/2026 | Impressora multifuncional colorida laser com suporte a impressão A3 e A4 | Epson | 1 | 7.400,00 | 7.400,00 | [PNCP](https://pncp.gov.br) |
| **Subtotal** | | | | **Subtotal Seção 4 (Estações e Periféricos)** | | | | **140.135,00** | |

---

## 3. Resumo Orçamentário por Macro-Categoria

| Macro-Categoria de Investimento | Subtotal (R$) | Participação Percentual (%) |
| :--- | :---: | :---: |
| **1. Ativos de Rede e Comunicação** | 18.839,60 | 6,87% |
| **2. Servidores Corporativos e Armazenamento Central** | 89.700,00 | 32,71% |
| **3. Gabinetes, Passivos e Cabeamento Estruturado** | 25.554,85 | 9,32% |
| **4. Estações de Trabalho e Periféricos de Pesquisa** | 140.135,00 | 51,10% |
| **VALOR TOTAL GLOBAL DO PROJETO** | **274.229,45** | **100,00%** |
