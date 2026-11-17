# Projeto de Infraestrutura de Rede e Plataforma Geoespacial

> **Instituição**: Universidade Federal de Sergipe (UFS)  
> **Centro / Departamento**: Centro de Ciências Exatas e Tecnologia (CCET)  
> **Disciplina**: Projeto de Redes de Computadores (Turma 2026.2)  
> **Responsável Técnico**: Diogo Santos Pires Jandiroba (`diogojandiroba@academico.ufs.br`)

---

## 1. Descrição Executiva do Projeto

Este projeto compreende o planejamento, especificação técnica, projeto lógico e físico de rede, orçamentação pública e implantação automatizada da infraestrutura de telecomunicações e serviços de dados voltada ao **Grupo de Pesquisa em Modelagem Hidrológica em Bacias Hidrográficas Nordestinas** da UFS.

A infraestrutura atende dois prédios universitários interligados por fibra óptica: o **Laboratório de Geoprocessamento e Sala de Servidores (CT-12, Sala 201)** e a **Sala dos Pesquisadores (CT-09, Sala 101)**, integrando a comutação, o roteamento de alta disponibilidade, segurança perimetral com firewall dedicado e a publicação de mapas interativos através da plataforma de código aberto **NextGIS Web**.

---

## 2. Contexto e Problema de Negócio

### O Cenário Atual
O grupo de pesquisa realiza simulações hidrológicas, estudos de impacto de resíduos sólidos em sistemas de drenagem urbana e mapeamento de bacias hidrográficas. Atualmente, os pesquisadores enfrentam:
* **Armazenamento Fragmentado**: Arquivos cartográficos pesados (*Shapefiles*, Modelos Digitais de Elevação e ortofotos) espalhados em computadores individuais sem controle de versão centralizado;
* **Sobrecarga de Licenciamento**: Dependência de softwares proprietários caros instalados isoladamente em cada estação de trabalho;
* **Rede Legada Insegura**: Falta de isolamento de tráfego, ausência de zonas de segurança perimetral (DMZ) e vulnerabilidade na integridade das bases de dados;
* **Dificuldade de Compartilhamento**: Ausência de um servidor de mapas web para publicação ágil de resultados científicos para a comunidade acadêmica e órgãos públicos gestores de recursos hídricos.

### Por que o Projeto é Necessário Agora?
Com a expansão dos projetos de pesquisa financiados e a necessidade de disponibilizar os dados de bacias hidrográficas em tempo real, a UFS demanda uma infraestrutura moderna, segura, auditável e dimensionada sob a **Lei nº 14.133/2021**, dotada de um servidor geoespacial autônomo baseado em software livre.

---

## 3. Objetivos do Projeto

* **Implantar Cabeamento Estruturado Cat6 e Fibra Óptica**: Conectar com alta confiabilidade as bancadas de pesquisa dos dois laboratórios (CT-09 e CT-12) com suporte a Gigabit Ethernet;
* **Estruturar Rede em Três Camadas com Zonas de Segurança**: Isolar o tráfego de estações de pesquisa, pontos de acesso sem fio (Wi-Fi 6), gerência de rede e a DMZ de servidores;
* **Prover Barreira de Segurança Perimetral**: Proteger os servidores corporativos com firewall físico (*stateful inspection*) e tradução de endereços (*NAT Overload*);
* **Automatizar a Solução NextGIS Web com Docker**: Subir de forma reproduzível a aplicação cartográfica com banco PostgreSQL/PostGIS e cache Redis;
* **Orçar com Fidelidade ao PNCP**: Cotar ativos e passivos a partir de Atas de Registro de Preços vigentes na Esfera Federal.

---

## 4. Escopo Resumido

### O que está incluso no projeto:
* Projeto Lógico de Rede com roteamento inter-VLAN, DHCP Relay e Listas de Controle de Acesso (ACL);
* Projeto de Segurança Perimetral com Cisco ASA 5506-X e regras de inspeção modular (MPF);
* Projeto Físico de Cabeamento Estruturado Categoria 6 (97 pontos de dados) e backbone óptico monomodo inter-predial de 300 metros;
* Layout de ocupação vertical de equipamentos no Rack 42U da Sala 201 (CT-12);
* Simulação e homologação completa no Cisco Packet Tracer;
* Automação multicontêiner (*Infrastructure as Code*) via Docker Compose da plataforma NextGIS Web e PostGIS;
* Lista Técnica de Materiais (BOM) e levantamento de atas no Portal Nacional de Contratações Públicas (PNCP).

### O que NÃO está incluso no projeto:
* Obras de alvenaria pesada ou reformas civis estruturais nos prédios (apenas adequação de eletrocalhas e mobiliário);
* Aquisição de enlaces WAN externos dedicados (a rede utiliza o link institucional já provido pela UFS/NTI);
* Customização de código-fonte interno do software NextGIS Web (utiliza-se a distribuição estável de código aberto).

---

## 5. Solução Proposta (Visão Geral)

### Resumo da Arquitetura: Como a Rede Funciona na Prática
A rede foi desenhada para que qualquer pesquisador ou estudante possa ligar seu computador à bancada ou conectar-se à rede sem fio corporativa e acessar instantaneamente os serviços cartográficos com máxima segurança:

1. Ao conectar o cabo na tomada de rede ou associar-se ao Wi-Fi corporativo, o computador recebe automaticamente um endereço IP através de um **servidor DHCP dedicado**, intermediado pelo roteador central;
2. As estações de trabalho navegam na Internet através de uma barreira dupla: passam pelo **Firewall Físico**, que verifica a legitimidade dos pacotes, e pelo **Roteador de Borda**, que traduz os endereços para o link da UFS;
3. As pesquisas e mapas são acessados diretamente pelo navegador web (`http://nextgis.labhidro.ufs.br`), que se comunica com o servidor de aplicação. Os dados brutos do banco de dados ficam confinados em uma zona restrita (DMZ), impedindo ataques ou manipulações não autorizadas.

```text
[ Internet / Provedor UFS ]
            │
            ▼ (Sub-rede WAN 200.17.0.0/30)
 ┌──────────────────────┐
 │  Roteador de Borda   │ (Cisco ISR 4321 com NAT Overload)
 └──────────┬───────────┘
            │
            ▼ (Enlace P2P 10.0.0.0/30)
 ┌──────────────────────┐
 │   Firewall Físico    │ (Cisco ASA 5506-X - Inspeção de Estado MPF)
 └──────────┬───────────┘
            │
            ▼ (Enlace P2P 10.0.1.0/30)
 ┌──────────────────────┐
 │   Roteador Interno   │ (Cisco 2911 - Roteamento Inter-VLAN e DHCP Relay)
 └──────────┬───────────┘
            │ Tronco 802.1Q (VLANs 10, 20, 30, 40)
            ▼
 ┌──────────────────────┐
 │ Switches e Acesso    │ ───► [ Servidores DMZ: NextGIS, PostGIS, DHCP ]
 │ (CT-12 e CT-09)      │ ───► [ Estações de Pesquisa e Wi-Fi Corporativo ]
 └──────────────────────┘
```

### Benefícios Diretos
* **Segurança Reforçada**: Isolamento completo entre a rede administrativa, as estações dos alunos e o banco de dados de pesquisa, com filtragem ativa de portas e inspeção de ameaças perimetrais;
* **Escalabilidade**: A segmentação em VLANs e a adoção de fibra óptica permitem a adição de dezenas de novos computadores sem degradação de desempenho;
* **Facilidade de Gerenciamento**: Endereçamento IP centralizado via DHCP Relay e administração remota segura restrita a computadores autorizados;
* **Velocidade e Confiabilidade**: Conexões Gigabit Ethernet (1000 Mbps) em todas as portas e tráfego inter-predial em fibra óptica monomodo imune a ruídos elétricos.

---

## 6. Estrutura de Navegação do Repositório

O repositório está organizado segundo as diretrizes de entrega da disciplina:

```text
├── README.md               # Esta página de apresentação executiva
├── docs/                   # Documentação técnica em Markdown com imagens
│   ├── projeto-logico.md   # Arquitetura lógica 3 camadas, VLANs e ACLs
│   ├── projeto-fisico.md   # Planta física, cabeamento e layout do Rack 42U
│   ├── bom-orcamento.md    # Lista de materiais (BOM) e atas do PNCP
│   ├── mecanismos-avaliacao.md # Homologação e testes empíricos
│   ├── adr/                # Architectural Decision Records (ADRs)
│   └── img/                # Diagramas, topologias e plantas
├── iac/                    # Infraestrutura como Código
│   ├── docker-compose.yml  # Automação da plataforma NextGIS Web
│   ├── nginx.conf          # Configuração do proxy reverso
│   └── manual-implantacao.md # Guia de instalação no Ubuntu / AWS EC2
├── landing-page/           # Catálogo de Software Livre (Wiki da Turma)
│   ├── README.md           # Ficha técnica da aplicação NextGIS Web
│   ├── manual-ubuntu.md    # Manual do pesquisador no Ubuntu
│   ├── comandos-teste.md   # Roteiro de testes de bancada do software
│   └── video-apresentacao.md # Roteiro e link do vídeo explicativo
├── scripts/                # Scripts de configuração dos ativos Cisco IOS / ASA
└── packer-tracker/         # Arquivos de simulação (.pkt) e topologias
```
