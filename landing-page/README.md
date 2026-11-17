# NextGIS Web — Plataforma Corporativa de Gestão e Publicação Geoespacial

> **Catálogo de Manuais de Software Livre da Turma (UFS 2026.2)**  
> **Software**: NextGIS Web  
> **Responsável Técnico**: Diogo Santos Pires Jandiroba (`diogojandiroba@academico.ufs.br`)  
> **Aplicação**: Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas (CCET/UFS)

---

## 1. Visão Geral do Software

O **NextGIS Web** é uma plataforma de servidor cartográfico e sistema de informação geográfica (*Web GIS*) de código aberto. Permite armazenar, catalogar, renderizar e publicar conjuntos de dados espaciais vetoriais (pontos, linhas e polígonos) e matriciais (*rasters* de elevação e imagens de satélite) diretamente pelo navegador web.

A plataforma implementa nativamente os padrões abertos do *Open Geospatial Consortium* (OGC):
* **WMS (*Web Map Service*)**: Publicação de mapas dinâmicos em camadas renderizadas;
* **WFS (*Web Feature Service*)**: Consulta direta e edição vetorial de atributos geográficos;
* **TMS (*Tile Map Service*)**: Geração de pirâmides de mosaicos de alta performance para clientes web e móveis.

---

## 2. Arquitetura da Solução

A solução opera de forma desacoplada em contêineres Docker:

```text
[ Usuário / Navegador Web / QGIS Desktop ]
                  │
                  ▼  (Porta 80 / 443 TCP)
           ┌──────────────┐
           │  Nginx Proxy │ (Terminação HTTP e Cache Estático)
           └──────┬───────┘
                  │
                  ▼  (Porta 8080 TCP)
         ┌─────────────────┐
         │   NextGIS Core  │ ◄──────► ┌─────────────┐
         │  (Servidor OGC) │          │ Redis Cache │ (Fila Assíncrona)
         └────────┬────────┘          └─────────────┘
                  │
                  ▼  (Porta 5432 TCP)
     ┌────────────────────────┐
     │ PostgreSQL 16 + PostGIS│ (Persistência Vetorial e Índices GIST)
     └────────────────────────┘
```

---

## 3. Principais Benefícios para o Laboratório

1. **Acesso Centralizado sem Necessidade de Instalação Local**: Pesquisadores e alunos visualizam e editam bases cartográficas diretamente pelo navegador sem dependência de licenças proprietárias;
2. **Integração Nativa com o QGIS**: Conexão direta aos projetos locais dos pesquisadores via serviços WMS/WFS;
3. **Escalabilidade e Desacoplamento**: O processamento pesado de consultas espaciais fica isolado no banco PostGIS, sem degradação na navegação do mapa;
4. **Segurança de Acesso e Perfilamento**: Gestão granular de permissões por grupo de pesquisa e camadas de dados.

---

## 4. Navegação e Documentação Rápida

* [Manual de Implantação e Operação no Ubuntu](manual-ubuntu.md)
* [Roteiro de Comandos e Testes de Homologação](comandos-teste.md)
* [Roteiro do Vídeo Demonstrativo](video-apresentacao.md)
* [Repositório da Automação (IaC)](../iac/docker-compose.yml)
* [Projeto de Redes e Infraestrutura](../docs/projeto-logico.md)
