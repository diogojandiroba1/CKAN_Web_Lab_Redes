import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import shutil

src = 'c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal.xlsx'
bak = 'c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal_original_omada.xlsx'
shutil.copyfile(src, bak)
print('Backup criado:', bak)

wb = openpyxl.load_workbook(src)
ws_idx = wb.sheetnames.index('Lista de equipamentos')
del wb['Lista de equipamentos']
ws = wb.create_sheet(title='Lista de equipamentos', index=ws_idx)

# Estilos
header_font = Font(name='Arial', size=10, bold=True, color='000000')
title_font = Font(name='Arial', size=12, bold=True, color='002060')
sub_font = Font(name='Arial', size=9, bold=True, color='FFFFFF')
data_font = Font(name='Arial', size=9, bold=False, color='000000')
bold_data_font = Font(name='Arial', size=9, bold=True, color='000000')

fill_orange = PatternFill(start_color='FFC000', end_color='FFC000', fill_type='solid') # Laranja Slide 8
fill_yellow = PatternFill(start_color='FFF2CC', end_color='FFF2CC', fill_type='solid')
fill_gray_header = PatternFill(start_color='EAEAEA', end_color='EAEAEA', fill_type='solid')
fill_section = PatternFill(start_color='1F497D', end_color='1F497D', fill_type='solid')

thin_border = Border(
    left=Side(style='thin', color='B0B0B0'),
    right=Side(style='thin', color='B0B0B0'),
    top=Side(style='thin', color='B0B0B0'),
    bottom=Side(style='thin', color='B0B0B0')
)

align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
align_right = Alignment(horizontal='right', vertical='center')

# Cabecalho do Projeto
ws['A1'] = 'PLANILHA ORCAMENTARIA EXECUTIVA (BILL OF MATERIALS - BOM) - INFRAESTRUTURA DE REDES UFS'
ws['A1'].font = title_font
ws['A2'] = 'Projeto: Laboratorio de Geoprocessamento e Modelagem Hidrologica (CT-09 e CT-12) | Autor: DIOGO SANTOS PIRES JANDIROBA | Base: Lei no 14.133/2021 (PNCP)'
ws['A2'].font = Font(name='Arial', size=9, italic=True, color='595959')

headers = [
    'Item',
    'Tipo Original (manter)',
    'Tipo Dispositivo',
    'Ata Vigente / ID de Contratacao PNCP',
    'Descricao e Modelo de Referencia',
    'Marca',
    'Qtd',
    'Copia Seg.',
    'Total',
    'Preco Unitario (R$)',
    'Desconto',
    'Preco Total (R$)',
    'Link / Fonte TR (PNCP)'
]

row = 4
for col_idx, h in enumerate(headers, 1):
    cell = ws.cell(row=row, column=col_idx, value=h)
    cell.font = header_font
    cell.alignment = align_center
    cell.border = thin_border
    if col_idx in [3, 4]: # Colunas Laranjas exigidas no Slide 8
        cell.fill = fill_orange
    elif col_idx in [10, 12]:
        cell.fill = fill_yellow
    else:
        cell.fill = fill_gray_header
ws.row_dimensions[row].height = 28

items_data = [
    # Secao 1: Ativos
    ('SEC', '1. ATIVOS DE REDE E COMUNICACAO (SIMULACAO OMADA E TR)', ''),
    ('1.1', 'ER7206', 'Roteador / Gateway VPN', '32752798000114-1-000028/2025', 'Roteador Gateway corporativo Multi-Gigabit VPN, Firewall SPI, Dual WAN', 'TP-LINK', 1, 0, 1, 2850.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('1.2', 'SG2210P', 'Switch PoE+ Gigabit', '32752798000114-1-000028/2025', 'Switch gerenciavel 10P GbE com 8 portas PoE+ (61W total) para APs', 'TP-LINK', 2, 0, 2, 1420.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('1.3', 'SG3428', 'Switch 24P Gigabit L2+', '32752798000114-1-000028/2025', 'Switch gerenciavel 24 portas Gigabit com 4 slots SFP 1G para agregacao', 'TP-LINK', 4, 0, 4, 2690.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('1.4', 'EAP610', 'Access Point Wi-Fi 6', '32752798000114-1-000028/2025', 'Access Point teto dual-band AX1800 Wi-Fi 6 Gigabit PoE (1x CT-09 e 1x CT-12)', 'TP-LINK', 2, 0, 2, 980.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('1.5', 'CAT.6', 'Cabo U/UTP Cat6 (m)', '32752798000114-1-000028/2025', 'Cabo de par trancado Categoria 6 23 AWG LSZH azul para ramais das bancadas', 'FURUKAWA', '24 m', 0, '24 m', 4.50, '0.00%', '108.00', 'https://pncp.gov.br'),
    ('1.6', 'SMF', 'Cabo Optico Monomodo (m)', '32752798000114-1-000028/2025', 'Cabo optico monomodo 9/125um geleado subterraneo interligacao CT09-CT12', 'FURUKAWA', '31 m', 0, '31 m', 12.00, '0.00%', '372.00', 'https://pncp.gov.br'),
    
    # Secao 2: Servidores
    ('SEC', '2. SERVIDORES CORPORATIVOS E ARMAZENAMENTO (SISTEMA NEXTGIS)', ''),
    ('2.1', '--', 'Servidor Web NextGIS 1U', '32752798000114-1-000028/2025', 'Servidor Rack 1U, Intel Xeon Silver, 64GB RAM DDR4 ECC, 2x 480GB SSD NVMe', 'DELL', 1, 0, 1, 24500.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('2.2', '--', 'Servidor Banco PostGIS 2U', '32752798000114-1-000028/2025', 'Servidor Rack 2U, Intel Xeon Silver, 128GB RAM DDR4 ECC, 4x 1.2TB SAS 10K RAID10', 'DELL', 1, 0, 1, 38900.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('2.3', '--', 'Servidor DHCP Dedicado 1U', '32752798000114-1-000028/2025', 'Servidor Rack 1U, Intel Xeon E-2324, 32GB RAM DDR4 ECC, 2x 240GB SSD SATA', 'DELL', 1, 0, 1, 16800.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('2.4', '--', 'Storage NAS Backup 4B', '32752798000114-1-000028/2025', 'Unidade NAS 4 Baias 16TB brutos RAID 5 para repositorio de copias de seguranca', 'QNAP', 1, 0, 1, 9500.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),

    # Secao 3: Passivos
    ('SEC', '3. GABINETES, PASSIVOS E CABEAMENTO ESTRUTURADO', ''),
    ('3.1', '--', 'Rack Fechado 42U (CT-09)', '32752798000114-1-000028/2025', 'Rack fechado 19pol 42U x 1000mm com porta de vidro temperado e exaustao (CT-09)', 'MAXELETRON', 1, 0, 1, 4800.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.2', '--', 'Mini-Rack 24U (CT-12)', '32752798000114-1-000028/2025', 'Gabinete padrao 19pol 24U x 670mm de piso/parede para agregacao CT-12', 'MAXELETRON', 1, 0, 1, 2200.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.3', '--', 'Patch Panel Cat6 24P', '32752798000114-1-000028/2025', 'Painel de manobra 24 portas RJ-45 Cat6 T568A/B com guia traseira de cabos', 'FURUKAWA', 5, 0, 5, 340.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.4', '--', 'Caixa Cabo Cat6 305m', '32752798000114-1-000028/2025', 'Caixa com 305m cabo U/UTP Cat6 23 AWG 4 pares capa LSZH azul GigaLan', 'FURUKAWA', 8, 0, 8, 890.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.5', '--', 'Conector Keystone Cat6', '32752798000114-1-000028/2025', 'Modulo conector femea Keystone RJ-45 Cat6 SohoPlus para espelhos', 'FURUKAWA', 120, 0, 120, 18.50, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.6', '--', 'Patch Cord Cat6 1,5m', '32752798000114-1-000028/2025', 'Cabo manobra Cat6 1,5m conectorizado de fabrica LSZH azul T568A', 'FURUKAWA', 100, 0, 100, 14.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.7', '--', 'Patch Cord Cat6 2,5m', '32752798000114-1-000028/2025', 'Cabo manobra Cat6 2,5m conectorizado de fabrica LSZH azul T568A', 'FURUKAWA', 30, 0, 30, 18.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.8', '--', 'Guia de Cabos 1U', '32752798000114-1-000028/2025', 'Organizador horizontal de cabos 1U fechado metalico padrao 19pol', 'FURUKAWA', 6, 0, 6, 55.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.9', '--', 'Regua PDU 12 Tomadas', '32752798000114-1-000028/2025', 'Calha PDU 12 tomadas 20A NBR 14136 com disjuntor bipolar para rack', 'APC/SMS', 3, 0, 3, 260.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.10', '--', 'DIO Optico 1U 24F', '32752798000114-1-000028/2025', 'Distribuidor Interno Optico 1U 24 fibras com acopladores LC-UPC', 'FURUKAWA', 2, 0, 2, 720.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.11', '--', 'Nobreak Senoidal 3kVA', '32752798000114-1-000028/2025', 'Nobreak senoidal online dupla conversao 3000VA / 2700W padrao rack 2U (CT-09)', 'SMS/APC', 1, 0, 1, 8900.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('3.12', '--', 'Nobreak Senoidal 1.5kVA', '32752798000114-1-000028/2025', 'Nobreak senoidal interativo 1500VA para rack secundario (CT-12)', 'SMS/APC', 1, 0, 1, 2450.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),

    # Secao 4: Estacoes
    ('SEC', '4. ESTACOES DE TRABALHO E PERIFERICOS DE PESQUISA', ''),
    ('4.1', '--', 'Workstation Modelagem', '32752798000114-1-000028/2025', 'Estacao de trabalho Core i7, 32GB RAM, SSD 1TB NVMe, GPU RTX 4060 para SIG', 'DELL', 15, 0, 15, 8200.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('4.2', '--', 'Monitor 27pol QHD IPS', '32752798000114-1-000028/2025', 'Monitor profissional 27 polegadas IPS QHD (2560x1440) com ajuste de altura', 'DELL', 15, 0, 15, 1850.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
    ('4.3', '--', 'Multifuncional Laser A3/A4', '32752798000114-1-000028/2025', 'Impressora multifuncional colorida laser com suporte a impressao A3/A4', 'EPSON', 1, 0, 1, 7400.00, '0.00%', '=G{r}*J{r}', 'https://pncp.gov.br'),
]

row = 5
subtotal_rows = []

for item in items_data:
    if item[0] == 'SEC':
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=13)
        cell = ws.cell(row=row, column=1, value=item[1])
        cell.font = sub_font
        cell.fill = fill_section
        cell.alignment = align_left
        ws.row_dimensions[row].height = 20
        row += 1
        continue
    
    code, original_type, dev_type, ata, desc, marca, qtd, copia, total_qtd, v_unit, desc_pct, v_total_formula, link = item
    
    ws.cell(row=row, column=1, value=code).alignment = align_center
    ws.cell(row=row, column=2, value=original_type).alignment = align_center
    
    # Coluna 3: Tipo Dispositivo (Laranja)
    c3 = ws.cell(row=row, column=3, value=dev_type)
    c3.alignment = align_left
    c3.fill = PatternFill(start_color='FFF2CC', end_color='FFF2CC', fill_type='solid')
    c3.font = bold_data_font
    
    # Coluna 4: Ata PNCP (Laranja)
    c4 = ws.cell(row=row, column=4, value=ata)
    c4.alignment = align_center
    c4.font = bold_data_font
    c4.hyperlink = link
    
    ws.cell(row=row, column=5, value=desc).alignment = align_left
    ws.cell(row=row, column=6, value=marca).alignment = align_center
    ws.cell(row=row, column=7, value=qtd).alignment = align_center
    ws.cell(row=row, column=8, value=copia).alignment = align_center
    ws.cell(row=row, column=9, value=total_qtd).alignment = align_center
    
    # Valores
    c10 = ws.cell(row=row, column=10, value=v_unit)
    c10.alignment = align_right
    c10.number_format = 'R$ #,##0.00'
    
    ws.cell(row=row, column=11, value=desc_pct).alignment = align_center
    
    c12 = ws.cell(row=row, column=12)
    if isinstance(v_total_formula, str) and v_total_formula.startswith('='):
        c12.value = v_total_formula.format(r=row)
    else:
        try:
            c12.value = float(v_total_formula)
        except:
            c12.value = v_total_formula
    c12.alignment = align_right
    c12.number_format = 'R$ #,##0.00'
    c12.font = bold_data_font
    subtotal_rows.append(row)
    
    c13 = ws.cell(row=row, column=13, value=link)
    c13.alignment = align_center
    c13.hyperlink = link
    c13.font = Font(name='Arial', size=8, color='0000FF', underline='single')
    
    for c in range(1, 14):
        cell_c = ws.cell(row=row, column=c)
        cell_c.border = thin_border
        if cell_c.font is None or cell_c.font.name != 'Arial':
            cell_c.font = data_font
            
    ws.row_dimensions[row].height = 22
    row += 1

# Linha de Total Geral
row += 1
ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=11)
total_label = ws.cell(row=row, column=1, value='VALOR TOTAL ESTIMADO DA INFRAESTRUTURA DE REDES E TI (R$):')
total_label.font = Font(name='Arial', size=10, bold=True, color='000000')
total_label.alignment = align_right

# Formula de soma de todas as linhas de produto
sum_formula = '+'.join([f'L{r}' for r in subtotal_rows])
total_cell = ws.cell(row=row, column=12, value=f'={sum_formula}')
total_cell.font = Font(name='Arial', size=11, bold=True, color='C00000')
total_cell.alignment = align_right
total_cell.number_format = 'R$ #,##0.00'
total_cell.fill = fill_yellow
total_cell.border = thin_border
ws.row_dimensions[row].height = 26

# Larguras das colunas
col_widths = {
    1: 7,   # Item
    2: 22,  # Tipo Original
    3: 26,  # Tipo Dispositivo (Laranja)
    4: 32,  # Ata PNCP (Laranja)
    5: 50,  # Descricao
    6: 14,  # Marca
    7: 10,  # Qtd
    8: 12,  # Copia Seg
    9: 10,  # Total
    10: 18, # Unit
    11: 10, # Desconto
    12: 20, # Total
    13: 22  # Link
}
for col, width in col_widths.items():
    ws.column_dimensions[get_column_letter(col)].width = width

wb.save(src)
print('Sucesso: Planilha NextGisWebFinal.xlsx formatada no padrao do Slide 8!')
