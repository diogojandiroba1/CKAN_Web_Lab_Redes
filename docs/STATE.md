# Estado do Projeto - Infraestrutura de Redes UFS

**Última Atualização**: 2026-11-17  
**Responsável**: Diogo Santos Pires Jandiroba  
**Status Geral**: Projeto Físico no TP-Link Omada e Planilha Orçamentária BOM Concluídos (v1.1.0)

---

## 1. Feito (Entregas e Ajustes Concluídos)

- [x] **Projeto Físico e Simulação no TP-Link Omada**:
  - Planta baixa importada e cotada para os dois prédios: **CT-09 (Sala 101, 55,82 m²)** e **CT-12 (Sala 201, 72,63 m²)**;
  - Rack Principal 42U alocado no **CT-09 (Sala 101)** contendo o Roteador Gateway ER7206, Switch PoE+ SG2210P, Switch de Agregação SG3428, Servidores Dell (NextGIS Web, PostGIS, DHCP) e Nobreak 3000VA;
  - Rack Secundário 24U alocado no **CT-12 (Sala 201)** contendo Switch PoE+ SG2210P, Switch de Acesso SG3428 e Nobreak 1500VA;
  - Cobertura Wi-Fi 6 dimensionada com 1x Ponto de Acesso TP-Link Omada EAP610 por sala, assegurando nível de sinal superior a $-60\text{ dBm}$ em 100% das bancadas de alunos;
  - Enlace de fibra óptica monomodo subterrâneo (SMF 31 metros) interligando os racks dos dois prédios.

- [x] **Planilha Orçamentária Executiva (BOM) Formatada (Slide 8)**:
  - Planilha [`NextGisWebFinal.xlsx`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal.xlsx) formatada com as colunas em destaque em laranja exigidas pela professora:
    - *Tipo Dispositivo*
    - *Ata Vigente / ID de Contratação PNCP*
  - Consolidação de 4 categorias:
    1. Ativos de Rede e Comunicação (R$ 18.890,00);
    2. Servidores Corporativos e Armazenamento Central NextGIS (R$ 89.700,00);
    3. Gabinetes, Passivos e Cabeamento Estruturado (R$ 33.880,00);
    4. Estações de Trabalho e Periféricos de Pesquisa (R$ 158.150,00);
  - **Valor Total Global Estimado**: **R$ 300.620,00**, fundamentado na Lei nº 14.133/2021 e em cotações públicas federais no PNCP (Ata nº 004/2025 - ID `32752798000114-1-000028/2025`);
  - Backup original do Omada preservado em [`NextGisWebFinal_original_omada.xlsx`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/NextGisWebFinal_original_omada.xlsx).

- [x] **Sincronização da Documentação Técnica e Relatório em LaTeX**:
  - [`docs/projeto-fisico.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/projeto-fisico.md) e [`docs/bom-orcamento.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/bom-orcamento.md) atualizados com tabelas de ativos e passivos;
  - Capítulo 4 (`04_Projeto_Fisico_Rede.tex`) e Capítulo 5 (`05_Projeto_Detalhado_Orcamento.tex`) alinhados com o orçamento de R$ 300.620,00;
  - Documento compilado com código 0 gerando [`Template_Unificado_LATEX/main.pdf`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/Template_Unificado_LATEX/main.pdf) (29 páginas).

- [x] **Infraestrutura em Nuvem AWS e Automação IaC**:
  - NextGIS Web Community Edition, PostGIS 15 e Redis operacionais na instância EC2 (`http://50.17.116.97`) na porta 80.

---

## 2. Próximos Passos
1. Gravar o vídeo demonstrativo de 3 a 5 minutos na SEMAC (24-26/nov) com base em [`landing-page/video-apresentacao.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/video-apresentacao.md);
2. Incluir a entrada do projeto na Wiki oficial da turma (`https://github.com/elan-git/catalogo/wiki`).
