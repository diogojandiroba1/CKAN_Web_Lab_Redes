# Estado do Projeto - Infraestrutura de Redes UFS

**Última Atualização**: 2026-11-17  
**Responsável**: Diogo Santos Pires Jandiroba  
**Status Geral**: Repositório Git Oficial Sincronizado e Publicado no GitHub (v1.0.0)

---

## 1. Feito (Entregas e Ajustes Concluídos)

- [x] **Publicação do Repositório Oficial no GitHub**:
  - Repositório remoto configurado: [`https://github.com/diogojandiroba1/NextGIS_Web_Lab_Redes.git`](https://github.com/diogojandiroba1/NextGIS_Web_Lab_Redes.git);
  - Branch principal padronizada como `main`;
  - Primeiro push realizado com sucesso (`git push -u origin main`);
  - Blindagem do [`.gitignore`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/.gitignore) assegurando zero vazamento de chaves privadas (`NextGIS_Web_chave.pem`), materiais internos de aula e temporários de compilação.

- [x] **Estrutura Completa de Diretórios Versionada**:
  - [`README.md`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/README.md) executivo e de negócios;
  - [`docs/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/docs/): `projeto-logico.md`, `projeto-fisico.md`, `bom-orcamento.md`, `mecanismos-avaliacao.md`, `adr/` e `img/`;
  - [`iac/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/iac/): `docker-compose.yml` (com `nextgis/nextgisweb-ce:latest`), `nginx.conf` e `manual-implantacao.md`;
  - [`landing-page/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/landing-page/): Ficha técnica formatada para o catálogo da turma (`elan-git/catalogo/wiki`), manuais do Ubuntu e roteiro do vídeo;
  - [`scripts/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/scripts/): Configurações Cisco IOS e ASA;
  - [`packer-tracker/`](file:///c:/Users/Diogo/Desktop/UFS_2026.2/Redes/packer-tracker/): Topologias `.pkt`.

- [x] **Validação em Nuvem (AWS EC2)**:
  - Instância pública no ar (`http://50.17.116.97`) respondendo na porta 80 via Nginx com a tela de login do NextGIS Web operacional.

---

## 2. Próximos Passos
1. Buscar números de atas e cotações no PNCP para atualizar `docs/bom-orcamento.md`;
2. Importar as plantas baixas no TP-Link Omada Designer para gerar o mapa de cobertura Wi-Fi;
3. Gravar o vídeo demonstrativo de 3 minutos e vincular à `landing-page/video-apresentacao.md`;
4. Adicionar o link do repositório na Wiki da turma (`https://github.com/elan-git/catalogo/wiki`).
