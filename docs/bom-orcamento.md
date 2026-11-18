# Lista Técnica de Materiais (BOM) e Orçamento PNCP

Apresenta-se a Lista Técnica de Materiais (*Bill of Materials*, BOM) e o orçamento da infraestrutura de redes projetada para os laboratórios de geoprocessamento e modelagem hidrológica nos prédios CT-09 e CT-12 da Universidade Federal de Sergipe (UFS).

Os valores unitários baseiam-se em Atas de Registro de Preços (ARP) e Pregões Eletrônicos federais vigentes no Portal Nacional de Contratações Públicas (PNCP), em conformidade com a Lei nº 14.133/2021. A planilha executiva completa está disponível em [`NextGisWebFinal.xlsx`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal.xlsx), estruturada no formato do software TP-Link Omada com as colunas complementares *Tipo Dispositivo* e *Ata Vigente / ID de Contratação PNCP* destacadas em cor laranja.

---

## 1. Atas e Pregões Federais Selecionados (Portal PNCP)

Os itens foram mapeados a partir de contratações públicas federais homologadas e vigentes:

| Órgão Gerenciador Federal | Processo / Pregão | Número da Ata | ID Contratação PNCP | Categoria Atendida | Link no PNCP |
| :--- | :--- | :---: | :---: | :--- | :---: |
| AGU (Advocacia-Geral da União) | PE SRP nº 11/2026 | Ata 07/2026 | `26994558000123-1-000147/2026-000001` | Switches, gateway VPN, fibras ópticas, patch cords, DIO e multifuncional | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| DNIT (Depto. Nac. Infraestrutura de Transportes) | PE SRP nº 90368/2025 | Ata 00011/2025 | `04892707000100-1-000453/2025-000002` | Cabos U/UTP Cat6 Furukawa, caixas 305 m, patch panels 24P e keystones | [Acessar Ata](https://pncp.gov.br/app/atas/04892707000100/2025/453/2) |
| Polícia Federal (MJSP - DTI/PF) | PE SRP nº 90004/2026 | Ata 00005/2026 | `00394494000136-1-000586/2026-000003` | Servidores rack 1U/2U (NextGIS Web, PostGIS, DHCP) e storage NAS | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/3) |
| Polícia Federal (MJSP - DTI/PF) | PE SRP nº 90004/2026 | Ata 00008/2026 | `00394494000136-1-000586/2026-000006` | Rack fechado 42U, guias horizontais 1U e réguas PDU 12 tomadas | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/6) |
| Embrapa (Agricultura Digital / Campinas) | PE SRP nº 90031/2025 | Ata 00031/2025 | `00348003000110-1-000689/2026-000001` | Nobreak senoidal online 3000 VA rack (PHD EA 3K) | [Acessar Ata](https://pncp.gov.br/app/atas/00348003000110/2026/689/1) |
| UFG (Universidade Federal de Goiás) | PE SRP nº 90026/2024 | Ata 00080/2025 | `01567601000143-1-000347/2024-000001` | Ponto de acesso corporativo Wi-Fi 6 PoE (EAP610) | [Acessar Ata](https://pncp.gov.br/app/atas/01567601000143/2024/347/1) |
| Exército Brasileiro (ESA / Três Corações) | PE SRP nº 90043/2025 | Ata 00037/2026 | `00394452000103-1-022077/2025-000004` | Mini-rack 24U de piso e nobreak senoidal 1500 VA | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/22077/4) |
| Exército Brasileiro (GRAFEX / Brasília) | PE SRP nº 90001/2026 | Ata 00001/2026 | `00394452000103-1-024864/2025-000001` | Estações de trabalho de modelagem Core i7 e monitores 27" QHD | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/24864/1) |

---

## 2. Planilha Orçamentária Consolidada (BOM)

### 2.1 Ativos de Rede e Comunicação (Simulação TP-Link Omada)

![Lista de Ativos e Quantitativos Exportados do TP-Link Omada](img/omada_lista_equipamentos.png)
*Link para a imagem anexada: [omada_lista_equipamentos.png](img/omada_lista_equipamentos.png)*  
*Planilha executiva formatada (Slide 8): [NextGisWebFinal.xlsx](../NextGisWebFinal.xlsx)*

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link no PNCP |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1.1 | ER7206 | Roteador / Gateway VPN | 26994558000123-1-000147/2026-000001 | Roteador corporativo Multi-Gigabit VPN, Firewall SPI, Dual WAN | TP-Link | 1 | 2.850,00 | 2.850,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 1.2 | SG2210P | Switch PoE+ Gigabit | 26994558000123-1-000147/2026-000001 | Switch gerenciável 10P GbE com 8 portas PoE+ (61W total) para APs | TP-Link | 2 | 1.420,00 | 2.840,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 1.3 | SG3428 | Switch 24P Gigabit L2+ | 26994558000123-1-000147/2026-000001 | Switch gerenciável 24 portas Gigabit com 4 slots SFP 1G para agregação | TP-Link | 4 | 2.690,00 | 10.760,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 1.4 | EAP610 | Access Point Wi-Fi 6 | 01567601000143-1-000347/2024-000001 | Access Point teto dual-band AX1800 Wi-Fi 6 Gigabit PoE (1x CT-09 e 1x CT-12) | TP-Link | 2 | 980,00 | 1.960,00 | [Acessar Ata](https://pncp.gov.br/app/atas/01567601000143/2024/347/1) |
| 1.5 | CAT.6 | Cabo U/UTP Cat6 (m) | 04892707000100-1-000453/2025-000002 | Cabo de par trançado Categoria 6 23 AWG LSZH azul para ramais das bancadas | Furukawa | 24 m | 2,40 | 57,60 | [Acessar Ata](https://pncp.gov.br/app/atas/04892707000100/2025/453/2) |
| 1.6 | SMF | Cabo Óptico Monomodo (m) | 26994558000123-1-000147/2026-000001 | Cabo óptico monomodo 9/125 $\mu$m geleado subterrâneo interligação CT09-CT12 | Furukawa | 31 m | 12,00 | 372,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| Subtotal | | | | Subtotal Categoria 1 (Ativos de Rede e Comunicação) | | | | 18.839,60 | |

O roteador de borda da operadora (`ISP-UFS`) não gera custo neste orçamento por pertencer à infraestrutura preexistente da rede metropolitana da UFS.

---

### 2.2 Servidores Corporativos e Armazenamento Central (Sistema NextGIS)

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link no PNCP |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 2.1 | -- | Servidor Web NextGIS 1U | 00394494000136-1-000586/2026-000003 | Servidor Rack 1U, Intel Xeon Silver, 64 GB RAM DDR4 ECC, 2x 480 GB SSD NVMe | Dell | 1 | 24.500,00 | 24.500,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/3) |
| 2.2 | -- | Servidor Banco PostGIS 2U | 00394494000136-1-000586/2026-000003 | Servidor Rack 2U, Intel Xeon Silver, 128 GB RAM DDR4 ECC, 4x 1.2 TB SAS 10K RAID 10 | Dell | 1 | 38.900,00 | 38.900,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/3) |
| 2.3 | -- | Servidor DHCP Dedicado 1U | 00394494000136-1-000586/2026-000003 | Servidor Rack 1U, Intel Xeon E-2324, 32 GB RAM DDR4 ECC, 2x 240 GB SSD SATA | Dell | 1 | 16.800,00 | 16.800,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/3) |
| 2.4 | -- | Storage NAS Backup 4B | 00394494000136-1-000586/2026-000003 | Unidade NAS 4 Baias 16 TB brutos RAID 5 para repositório de cópias de segurança | QNAP | 1 | 9.500,00 | 9.500,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/3) |
| Subtotal | | | | Subtotal Categoria 2 (Servidores e Armazenamento Central) | | | | 89.700,00 | |

---

### 2.3 Gabinetes, Passivos e Cabeamento Estruturado

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link no PNCP |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 3.1 | -- | Rack Fechado 42U (CT-09) | 00394494000136-1-000586/2026-000006 | Rack fechado 19" 42U x 1000 mm com porta de vidro temperado e exaustão (CT-09) | MaxEletron | 1 | 4.800,00 | 4.800,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/6) |
| 3.2 | -- | Mini-Rack 24U (CT-12) | 00394452000103-1-022077/2025-000004 | Gabinete padrão 19" 24U x 670 mm de piso/parede soldado para 400 kg | MaxEletron | 1 | 1.189,00 | 1.189,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/22077/4) |
| 3.3 | -- | Patch Panel Cat6 24P | 04892707000100-1-000453/2025-000002 | Painel de manobra 24 portas RJ-45 Cat6 T568A/B Multilan Furukawa | Furukawa | 5 | 110,57 | 552,85 | [Acessar Ata](https://pncp.gov.br/app/atas/04892707000100/2025/453/2) |
| 3.4 | -- | Caixa Cabo Cat6 305m | 04892707000100-1-000453/2025-000002 | Caixa com 305 m cabo U/UTP Cat6 23 AWG 4 pares capa LSZH azul (R$ 2,40/m) | Furukawa | 8 | 732,00 | 5.856,00 | [Acessar Ata](https://pncp.gov.br/app/atas/04892707000100/2025/453/2) |
| 3.5 | -- | Conector Keystone Cat6 | 04892707000100-1-000453/2025-000002 | Módulo conector fêmea Keystone RJ-45 Cat6 SohoPlus para espelhos | Furukawa | 120 | 18,50 | 2.220,00 | [Acessar Ata](https://pncp.gov.br/app/atas/04892707000100/2025/453/2) |
| 3.6 | -- | Patch Cord Cat6 1,5m | 26994558000123-1-000147/2026-000001 | Cabo manobra Cat6 1,5 m conectorizado de fábrica LSZH azul T568A | Furukawa | 100 | 14,00 | 1.400,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 3.7 | -- | Patch Cord Cat6 2,5m | 26994558000123-1-000147/2026-000001 | Cabo manobra Cat6 2,5 m conectorizado de fábrica LSZH azul T568A | Furukawa | 30 | 18,00 | 540,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 3.8 | -- | Guia de Cabos 1U | 00394494000136-1-000586/2026-000006 | Organizador horizontal de cabos 1U fechado metálico padrão 19" | Furukawa | 6 | 55,00 | 330,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/6) |
| 3.9 | -- | Régua PDU 12 Tomadas | 00394494000136-1-000586/2026-000006 | Calha PDU 12 tomadas 20A NBR 14136 com disjuntor bipolar para rack | APC / SMS | 3 | 260,00 | 780,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394494000136/2026/586/6) |
| 3.10 | -- | DIO Óptico 1U 24F | 26994558000123-1-000147/2026-000001 | Distribuidor Interno Óptico 1U 24 fibras com acopladores LC-UPC | Furukawa | 2 | 720,00 | 1.440,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| 3.11 | -- | Nobreak Senoidal 3kVA | 00348003000110-1-000689/2026-000001 | Nobreak senoidal online dupla conversão 3000 VA / 2700 W padrão rack 2U (PHD EA 3K) | PHD / SMS | 1 | 4.997,00 | 4.997,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00348003000110/2026/689/1) |
| 3.12 | -- | Nobreak Senoidal 1.5kVA | 00394452000103-1-022077/2025-000004 | Nobreak senoidal interativo 1500 VA para rack secundário (CT-12) | TS Shara | 1 | 1.450,00 | 1.450,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/22077/4) |
| Subtotal | | | | Subtotal Categoria 3 (Passivos e Infraestrutura) | | | | 25.554,85 | |

---

### 2.4 Estações de Trabalho e Periféricos de Pesquisa

| Item | Tipo Original | Tipo Dispositivo | Ata Vigente / ID PNCP | Descrição Técnica e Modelo de Referência | Marca | Qtd | Preço Unit. (R$) | Preço Total (R$) | Link no PNCP |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 4.1 | -- | Workstation Modelagem | 00394452000103-1-024864/2025-000001 | Estação de trabalho Core i7, 32 GB RAM, SSD 1 TB NVMe, GPU RTX 4060 para SIG | Dell / Exército | 15 | 6.999,00 | 104.985,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/24864/1) |
| 4.2 | -- | Monitor 27" QHD IPS | 00394452000103-1-024864/2025-000001 | Monitor profissional 27 polegadas IPS QHD (2560x1440) com ajuste de altura | Dell / Exército | 15 | 1.850,00 | 27.750,00 | [Acessar Ata](https://pncp.gov.br/app/atas/00394452000103/2025/24864/1) |
| 4.3 | -- | Multifuncional Laser A3/A4 | 26994558000123-1-000147/2026-000001 | Impressora multifuncional colorida laser com suporte a impressão A3 e A4 | Epson | 1 | 7.400,00 | 7.400,00 | [Acessar Ata](https://pncp.gov.br/app/atas/26994558000123/2026/147/1) |
| Subtotal | | | | Subtotal Categoria 4 (Estações e Periféricos) | | | | 140.135,00 | |

---

## 3. Resumo Orçamentário por Categoria de Investimento

| Categoria de Investimento | Subtotal (R$) | Participação (%) |
| :--- | :---: | :---: |
| 1. Ativos de Rede e Comunicação | 18.839,60 | 6,87% |
| 2. Servidores Corporativos e Armazenamento Central | 89.700,00 | 32,71% |
| 3. Gabinetes, Passivos e Cabeamento Estruturado | 25.554,85 | 9,32% |
| 4. Estações de Trabalho e Periféricos de Pesquisa | 140.135,00 | 51,10% |
| Total Global do Projeto | 274.229,45 | 100,00% |

---

## 4. Critérios Metodológicos de Dimensionamento

1. **Precificação Governamental**: Cada item do orçamento foi cotado a partir do menor preço unitário registrado em Ata de Registro de Preços federal vigente no PNCP, garantindo exequibilidade orçamentária e conformidade com os artigos da Lei nº 14.133/2021.
2. **Capacidade e Expansão Física**: O dimensionamento do cabeamento horizontal e dos módulos nos *patch panels* inclui 25% de portas reservas por sala para expansão de novos pontos de rede sem necessidade de troca estrutural.
3. **Autonomia Elétrica**: O nobreak online de dupla conversão de 3000 VA alocado no rack principal (CT-09) e a unidade interativa senoidal de 1500 VA no rack secundário (CT-12) foram dimensionados para fornecer tempo de sustentação mínimo de 20 minutos sob carga nominal, viabilizando o desligamento programado dos nós de computação durante eventuais interrupções no fornecimento da concessionária.

