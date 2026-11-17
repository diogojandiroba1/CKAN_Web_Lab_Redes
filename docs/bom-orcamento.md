# Lista Técnica de Materiais (BOM) e Orçamento PNCP

Este documento consolida a Lista Técnica de Materiais (*Bill of Materials* - BOM) dimensionada para a infraestrutura dos laboratórios nos prédios CT-09 e CT-12, acompanhada do levantamento orçamentário baseado em **Atas de Registro de Preços (ARP) vigentes na Esfera Federal** extraídas do Portal Nacional de Contratações Públicas (PNCP), em conformidade com a Lei nº 14.133/2021.

---

## 1. Planilha Orçamentária de Ativos de Rede e Servidores

Tabela orçamentária estruturada com as colunas padronizadas de contratação pública:

| Item | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca / Modelo | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte Oficial |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **1.1** | Roteador de Borda | A preencher | Roteador corporativo modular WAN com 2 portas Gigabit Ethernet e VPN IPsec | Cisco ISR 4321 | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **1.2** | Firewall Físico | A preencher | Firewall corporativo com 8 portas GbE, inspeção de estado com MPF e throughput > 250 Mbps | Cisco ASA 5506-X | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **1.3** | Roteador Interno | A preencher | Roteador de distribuição com 3 portas GbE nativas, suporte a 802.1Q e DHCP Relay | Cisco 2911 | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **1.4** | Switch Gerenciável | A preencher | Switch de acesso camada 2 com 24 portas 10/100/1000 Mbps e portas Gigabit SFP de uplink | Cisco Catalyst 2960-24TT | 4 | -- | -- | [PNCP](https://pncp.gov.br) |
| **1.5** | Switch PoE+ | A preencher | Switch gerenciável 8 portas Gigabit PoE+ 802.3at (potência total > 60W) para APs | TP-Link Omada SG2210P | 2 | -- | -- | [PNCP](https://pncp.gov.br) |
| **1.6** | Access Point Wi-Fi 6 | A preencher | Ponto de acesso teto dual band Wi-Fi 6 (AX1800), Gigabit Ethernet PoE | TP-Link Omada EAP610 | 3 | -- | -- | [PNCP](https://pncp.gov.br) |
| **2.1** | Servidor Web 1U | A preencher | Servidor rack 1U, Intel Xeon, 64 GB RAM DDR4 ECC, 2x 480 GB SSD NVMe (NextGIS Core e Nginx) | Dell PowerEdge R440/R450 | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **2.2** | Servidor Banco 2U | A preencher | Servidor rack 2U, Intel Xeon, 128 GB RAM DDR4 ECC, 4x 1.2 TB SAS 10K RAID 10 (PostgreSQL/PostGIS) | Dell PowerEdge R540/R550 | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **2.3** | Servidor DHCP 1U | A preencher | Servidor rack 1U, Intel Xeon, 32 GB RAM DDR4 ECC, 2x 240 GB SSD SATA (Serviços DHCP/DNS/NTP) | Dell PowerEdge R250/R350 | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **2.4** | Storage Backup NAS | A preencher | Unidade de armazenamento NAS 4 baias, 16 TB brutos em RAID 5 para repositório de cópias de segurança | QNAP / Synology 4B | 1 | -- | -- | [PNCP](https://pncp.gov.br) |

> **Nota sobre o Roteador de Borda da Operadora (`ISP-UFS`)**: O equipamento `ISP-UFS` não integra as despesas deste projeto por tratar-se de ativo de telecomunicações preexistente da rede metropolitana da Universidade Federal de Sergipe.

---

## 2. Planilha Orçamentária de Passivos, Cabeamento e Estações

| Item | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca / Modelo | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link / Fonte Oficial |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **3.1** | Rack 42U | A preencher | Gabinete fechado padrão 19 polegadas 42U x 1000 mm com porta de vidro e ventilação forçada | MaxEletron / GP Racks | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.2** | Rack 24U | A preencher | Gabinete fechado padrão 19 polegadas 24U x 670 mm para o Prédio CT-09 | MaxEletron / GP Racks | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.3** | Patch Panel Cat6 | A preencher | Painel de manobra 24 portas RJ-45 Categoria 6 com guia traseira | Furukawa SohoPlus 24P | 5 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.4** | Bobina Cabo Cat6 | A preencher | Caixa com 305 metros de cabo de par trançado U/UTP Cat6 23 AWG 4 pares LSZH azul | Furukawa GigaLan LSZH | 8 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.5** | Conector Keystone | A preencher | Módulo conector fêmea Keystone RJ-45 Cat6 T568A/B para espelhos | Furukawa SohoPlus Cat6 | 120 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.6** | Patch Cord 1,5m | A preencher | Cabo de manobra conectorizado de fábrica Cat6 1,5 m LSZH azul | Furukawa Cat6 1,5m | 100 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.7** | Patch Cord 2,5m | A preencher | Cabo de manobra conectorizado de fábrica Cat6 2,5 m LSZH azul | Furukawa Cat6 2,5m | 30 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.8** | Guia de Cabos 1U | A preencher | Organizador horizontal de cabos 1U fechado para rack 19" | Furukawa / D-Net 1U | 6 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.9** | Régua PDU | A preencher | Calha de tomadas PDU com 12 tomadas 20A NBR 14136 e disjuntor bipolar | APC / SMS PDU 12T | 3 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.10**| DIO Óptico 1U | A preencher | Distribuidor Interno Óptico 1U 24 fibras com acopladores LC-UPC | Furukawa TeraLan DIO | 2 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.11**| Cabo Óptico 6FO | A preencher | Cabo óptico monomodo SMF 9/125 $\mu$m geleado para duto subterrâneo (metros) | Furukawa CFOAC-SM | 300 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.12**| Nobreak 3000VA | A preencher | Nobreak senoidal online dupla conversão 3000 VA / 2700 W padrão rack 2U | SMS / APC On-Line 3kVA | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **3.13**| Nobreak 1500VA | A preencher | Nobreak senoidal interativo 1500 VA para rack do Prédio CT-09 | SMS / APC 1500VA | 1 | -- | -- | [PNCP](https://pncp.gov.br) |
| **4.1** | Workstation Pesquisa | A preencher | Estação de trabalho Core i7, 32 GB RAM, SSD NVMe 1 TB, GPU RTX 4060 para SIG e modelagem | Dell Precision / Lenovo | 15 | -- | -- | [PNCP](https://pncp.gov.br) |
| **4.2** | Monitor 27" QHD | A preencher | Monitor profissional 27 polegadas IPS QHD (2560x1440) com suporte ergonômico | Dell UltraSharp 27 | 15 | -- | -- | [PNCP](https://pncp.gov.br) |
| **4.3** | Impressora A3/A4 | A preencher | Impressora multifuncional colorida laser com suporte a impressão cartográfica A3 e A4 | Epson / HP Enterprise | 1 | -- | -- | [PNCP](https://pncp.gov.br) |

---

## 3. Metodologia de Cotação de Preços Públicos

1. **Consulta às Atas do PNCP**: As buscas são efetuadas no Portal Nacional de Contratações Públicas (`https://pncp.gov.br/app/atas?status=vigente&esferas=F`), priorizando a **Esfera Federal**;
2. **Homologação e Vigência**: Cada item utiliza como parâmetro atas com vigência ativa de 12 meses registradas por órgãos federais (como universidades, institutos federais e ministérios);
3. **Registro do ID de Contratação**: Os códigos de identificação de compra (ex.: `32752798000114-1-000028/2025`) são vinculados diretamente às planilhas geradas pelo software TP-Link Omada.
