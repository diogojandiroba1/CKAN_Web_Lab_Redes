# Vídeo Demonstrativo do Software Livre

> **Disciplina**: Projeto de Redes de Computadores (Turma 2026.2)  
> **Aluno / Responsável**: Diogo Santos Pires Jandiroba  
> **Software**: NextGIS Web  
> **Link do Vídeo**: `[Adicionar Link do Vídeo Aqui - YouTube / Google Drive / Loom]`

---

## Roteiro de Gravação Sugerido (Duração: 3 a 5 minutos)

### 1. Introdução (30 segundos)
* Apresentação pessoal (nome, curso, disciplina de Projeto de Redes na UFS);
* Apresentação do software escolhido (**NextGIS Web**) e o contexto do cliente (Grupo de Pesquisa em Modelagem Hidrológica do CCET/UFS);
* Objetivo da implantação: fornecer um servidor geográfico web para publicação de mapas e análise de recursos hídricos.

### 2. Infraestrutura e Automação (1 minuto)
* Mostrar rapidamente o terminal com os contêineres Docker em execução (`docker compose ps`);
* Explicar de forma simples o desacoplamento das camadas:
  * Nginx como proxy de entrada e cache;
  * NextGIS Core processando os serviços cartográficos;
  * PostgreSQL com PostGIS armazenando as geometrias e atributos espaciais;
  * Redis gerenciando tarefas assíncronas.

### 3. Demonstração Prática na Interface Web (2 a 3 minutos)
* Abrir o navegador e acessar o endereço da aplicação (local ou IP público da AWS EC2);
* Fazer login com as credenciais de administrador;
* Mostrar a estrutura de pastas dos recursos;
* Realizar o upload rápido de um arquivo Shapefile ou GeoJSON de drenagem/bacia hidrográfica;
* Abrir o visualizador de mapas web e interagir com o mapa (zoom in, zoom out, alternância de camadas e consulta de atributos);
* Demonstrar a geração da URL WMS para consumo no QGIS.

### 4. Conclusão (30 segundos)
* Destacar os ganhos práticos da solução: centralização de dados, custo zero de licenciamento, facilidade de acesso via navegador para qualquer pesquisador e conformidade com as políticas de segurança da rede projetada.
