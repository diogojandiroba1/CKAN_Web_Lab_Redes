# Estado do Projeto - Infraestrutura de Redes UFS

**Última Atualização**: 2026-11-17  
**Responsável**: Diogo Santos Pires Jandiroba  
**Status Geral**: Repositório Git Estruturado no Padrão Oficial da Disciplina (v1.0.0)

---

## 1. Feito (Entregas e Ajustes Concluídos)

- [x] **Estruturação do Repositório Git Oficial (Padrão Turma 2026.2)**:
  - Repositório inicializado com controle de versão local (`git init`);
  - Arquivo [`.gitignore`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/.gitignore) configurado para proteger chaves privadas (`*.pem`), materiais de aula do Google Classroom (`Formularios_atividades/`, PDFs de formulários, cronogramas) e temporários de compilação LaTeX;
  - Criação do [`README.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/README.md) executivo na raiz com Descrição, Responsável Técnico, Contexto/Problema de Negócio, Objetivos, Escopo (Incluso/Não Incluso), Solução Proposta sem jargões, Benefícios Diretos e Mapa do Repositório.

- [x] **Documentação Técnica em Markdown (`docs/`)**:
  - [`docs/projeto-logico.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/projeto-logico.md): Arquitetura hierárquica em três camadas (Core, Distribuição, Acesso) e zona perimetral de segurança (agnóstica a locais físicos), plano de endereçamento, VLANs, matriz de fluxos/ACLs e arquitetura de software livre;
  - [`docs/projeto-fisico.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/projeto-fisico.md): Planta baixa executiva, quantitativo de pontos por sala, cabeamento horizontal Cat6, fibra óptica monomodo e layout vertical do Rack 42U em diagrama ASCII escala U;
  - [`docs/bom-orcamento.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/bom-orcamento.md): Lista técnica de materiais (BOM) e tabela orçamentária baseada em Atas de Registro de Preços vigentes do PNCP (Esfera Federal);
  - [`docs/mecanismos-avaliacao.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/mecanismos-avaliacao.md): Roteiro e resultados de 8 ensaios empíricos de conectividade, inter-VLAN, bloqueio de portas, saída WAN e DHCP Relay;
  - Diretório [`docs/img/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/img/): Imagens e diagramas vinculados diretamente aos arquivos Markdown.

- [x] **Automação e Infraestrutura como Código (`iac/`)**:
  - [`iac/docker-compose.yml`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/iac/docker-compose.yml): Orquestração multicontêiner com NextGIS Web, PostgreSQL 16 com PostGIS 3.4, Redis 7.2 e Nginx Proxy;
  - [`iac/nginx.conf`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/iac/nginx.conf): Configuração de terminação HTTP e cache de recursos estáticos;
  - [`iac/manual-implantacao.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/iac/manual-implantacao.md): Manual detalhado de instalação do Docker e inicialização do ambiente no Ubuntu Server / AWS EC2.

- [x] **Catálogo e Wiki do Software Livre (`landing-page/`)**:
  - [`landing-page/README.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/README.md): Ficha técnica e resumo executivo padronizado para a Wiki da turma (`https://github.com/elan-git/catalogo/wiki`);
  - [`landing-page/manual-ubuntu.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/manual-ubuntu.md): Manual de operação do pesquisador no Ubuntu;
  - [`landing-page/comandos-teste.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/comandos-teste.md): Passo a passo com comandos de teste da aplicação, banco e API REST;
  - [`landing-page/video-apresentacao.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/video-apresentacao.md): Roteiro estruturado de 3 a 5 minutos para a gravação do vídeo demonstrativo.

---

## 2. Próximos Passos
1. Subida da aplicação NextGIS Web na instância EC2 da AWS utilizando a chave `NextGIS_Web_chave.pem`;
2. Exportação do projeto físico e cobertura Wi-Fi no software TP-Link Omada Designer;
3. Preenchimento dos números de atas do PNCP na planilha BOM (`docs/bom-orcamento.md`);
4. Gravação do vídeo curto de demonstração e inclusão do link em `landing-page/video-apresentacao.md`.
