# Manual de Instalação e Operação no Ubuntu Server

Este guia orienta a instalação passo a passo e o uso cotidiano da plataforma NextGIS Web no sistema operacional Ubuntu (versões 22.04 LTS ou 24.04 LTS).

---

## 1. Instalação Automatizada

Para inicializar a plataforma no Ubuntu via Docker Compose:

```bash
# Clone ou acesse o repositório do projeto
cd iac/

# Suba todos os serviços em segundo plano
docker compose up -d

# Valide se todos os contêineres estão no estado 'Up'
docker compose ps
```

---

## 2. Primeiro Acesso e Configuração da Plataforma

1. Abra o navegador web de sua preferência;
2. Acesse o endereço IP ou nome de host do servidor (ex.: `http://<IP-DO-SERVIDOR>`);
3. No canto superior direito, clique em **Entrar** (*Sign In*);
4. Credenciais padrão de primeiro acesso:
   * **Usuário**: `administrator`
   * **Senha**: `admin`
5. **Ação Recomendada**: Acesse o painel de administração de usuários e altere a senha padrão imediatamente.

---

## 3. Fluxo de Trabalho do Pesquisador

### A. Criando Pastas e Organizando Projetos
1. No menu lateral esquerdo, clique no botão **Criar Recurso**;
2. Selecione **Grupo de Recursos** (*Resource Group*);
3. Dê um nome para a pasta (ex.: `Bacia_Rio_Sergipe`) e clique em **Criar**.

### B. Importação de Camadas Vetoriais (Shapefiles / GeoJSON)
1. Dentro do grupo de recursos criado, clique em **Criar Recurso** $\rightarrow$ **Camada Vetorial**;
2. Selecione o arquivo `.zip` contendo os quatro arquivos obrigatórios do Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`) ou um arquivo `.geojson`;
3. O sistema detectará automaticamente o Sistema de Referência de Coordenadas (CRS) (ex.: SIRGAS 2000 / UTM 24S - EPSG:31984);
4. Clique em **Salvar**.

### C. Criação de Mapas Interativos Web
1. No grupo de recursos, selecione **Criar Recurso** $\rightarrow$ **Mapa Web**;
2. Adicione as camadas vetoriais que compõem o estudo sobre o mapa base (OpenStreetMap);
3. Defina a extensão e o nível de zoom inicial;
4. Clique em **Salvar**. O link gerado pode ser compartilhado com os pesquisadores da equipe.

---

## 4. Consumo de Dados no QGIS Desktop

Pesquisadores que utilizam o QGIS em suas estações de trabalho locais podem consumir as camadas diretamente do servidor sem precisar baixar os arquivos:

1. No NextGIS Web, abra as propriedades da camada desejada e copie a **URL WMS** ou **URL WFS**;
2. No QGIS Desktop, acesse o menu superior: **Camada** $\rightarrow$ **Adicionar Camada** $\rightarrow$ **Adicionar Camada WMS/WMTS**;
3. Crie uma nova conexão colando a URL e informando o nome da camada;
4. Clique em **Conectar**, selecione as feições desejadas e adicione à área de trabalho.
