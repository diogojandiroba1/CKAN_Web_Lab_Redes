# Mecanismos de Avaliação e Homologação da Rede

Este documento descreve os procedimentos de testes e validação empírica da infraestrutura corporativa, cobrindo conectividade de camada de enlace, roteamento inter-VLAN, filtragem por listas de controle de acesso (ACL), inspeção perimetral no firewall Cisco ASA 5506-X, tradução NAT/PAT e concessão dinâmica de endereços via DHCP Relay.

---

## 1. Metodologia de Testes

Os testes foram realizados por meio de comandos de terminal (CLI) disparados a partir das estações de trabalho e consoles dos ativos de rede no simulador Cisco Packet Tracer, validando os requisitos funcionais e de segurança da rede.

---

## 2. Roteiro e Resultados dos Testes de Conectividade

### Teste 01: Conectividade Intra-VLAN e Alcance do Gateway
* **Objetivo**: Verificar a comutação de quadros na VLAN 30 e a resposta da subinterface do roteador `router_interno`.
* **Origem**: Estação de Pesquisa `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Gateway padrão da rede de pesquisa (`192.168.30.1`)
* **Comando**:
  ```cmd
  ping 192.168.30.1
  ```
* **Resultado**:
  ```text
  Reply from 192.168.30.1: bytes=32 time<1ms TTL=255
  Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
  ```
* **Status**: **Aprovado** (0% de perda, tempo < 1 ms).

---

### Teste 02: Roteamento Inter-VLAN (Pesquisa para Servidores)
* **Objetivo**: Validar o roteamento 802.1Q entre a VLAN 30 e a VLAN 20.
* **Origem**: Estação de Pesquisa `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Servidor NextGIS Web `SRV-NEXTGIS` (`192.168.20.10`)
* **Comando**:
  ```cmd
  ping 192.168.20.10
  ```
* **Resultado**:
  ```text
  Reply from 192.168.20.10: bytes=32 time<1ms TTL=127
  Packets: Sent = 4, Received = 3, Lost = 1 (25% loss inicial por ARP)
  ```
* **Status**: **Aprovado** (comunicação estabelecida com sucesso).

---

### Teste 03: Rastreamento de Saltos e Travessia Perimetral (Traceroute)
* **Objetivo**: Mapear o percurso dos pacotes originados nas estações internas até a saída externa, comprovando a passagem pelo firewall e roteador de borda.
* **Origem**: Estação `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Destino externo de teste (`8.8.8.8`)
* **Comando**:
  ```cmd
  tracert 8.8.8.8
  ```
* **Resultado**:
  ```text
  1   <1 ms   <1 ms   <1 ms   192.168.30.1    (router_interno)
  2   <1 ms   <1 ms   <1 ms   10.0.1.1        (Firewall ASA 5506-X inside)
  3   <1 ms   <1 ms   <1 ms   10.0.0.1        (router_border ISR 4321)
  4   <1 ms   <1 ms   <1 ms   200.17.0.1      (ISP-UFS Provedor)
  Trace complete.
  ```
* **Status**: **Aprovado** (travessia ordenada pelos 4 saltos de rede).

---

## 3. Roteiro e Resultados dos Testes de Segurança

### Teste 04: Acesso às Portas Web do NextGIS (HTTP / HTTPS)
* **Objetivo**: Confirmar que as portas 80 e 443 TCP estão liberadas para acesso dos usuários.
* **Origem**: Estação de Pesquisa ou notebook Wi-Fi
* **Destino**: Servidor `SRV-NEXTGIS` (`192.168.20.10`)
* **Ação**: Abertura da URL `http://192.168.20.10` no navegador web do computador.
* **Resultado**: Interface web do NextGIS Web carregada com sucesso; camadas e mapas interativos exibidos sem bloqueios.
* **Status**: **Aprovado**.

---

### Teste 05: Bloqueio do Banco de Dados Relacional e Espacial (TCP 5432)
* **Objetivo**: Garantir que as estações não consigam estabelecer conexão direta com a porta nativa do PostgreSQL.
* **Origem**: Estação `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Servidor PostGIS `SRV-POSTGIS` (`192.168.20.20`)
* **Ação**: Tentativa de conexão na porta 5432 via cliente telnet ou socket TCP.
* **Resultado**: Conexão rejeitada e descartada pelo roteador interno por força da regra `deny tcp host 192.168.20.20 eq 5432 log`.
* **Status**: **Aprovado**.

---

### Teste 06: Isolamento da Sub-rede de Gerência de Ativos (VLAN 10)
* **Objetivo**: Impedir que estações comuns alcancem portas e IPs de gerenciamento de switches e roteadores.
* **Origem**: Estação `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Interface de gerência do switch `SW-CT12` (`192.168.10.2`)
* **Comando**:
  ```cmd
  ping 192.168.10.2
  ```
* **Resultado**:
  ```text
  Reply from 192.168.30.1: Destination host unreachable.
  Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
  ```
* **Status**: **Aprovado** (descarte realizado pelo gateway da rede antes do roteamento para a VLAN 10).

---

### Teste 07: Conectividade WAN e Saída para Internet (NAT/PAT e MPF)
* **Objetivo**: Validar a saída externa, inspeção de estado no ASA 5506-X e tradução por sobrecarga (NAT) no Cisco ISR 4321.
* **Origem**: Estação `WS-CT12-01` (`192.168.30.50`)
* **Destino**: Gateway WAN do Provedor (`200.17.0.1`) e DNS público simulado (`8.8.8.8`)
* **Comando**:
  ```cmd
  ping 200.17.0.1
  ping 8.8.8.8
  ```
* **Resultado**:
  ```text
  Reply from 200.17.0.1: bytes=32 time<1ms TTL=252
  Reply from 8.8.8.8: bytes=32 time<1ms TTL=252
  Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
  ```
* **Status**: **Aprovado** (tradução NAT confirmada e retorno inspecionado com sucesso).

---

### Teste 08: Concessão Dinâmica de Endereços via DHCP Relay
* **Objetivo**: Validar a concessão de IP pelo servidor dedicado `SRV-DHCP` para estações remotas no Prédio CT-09.
* **Origem**: Estação remota `WS-CT09-01`
* **Procedimento**: Seleção do modo `DHCP` na interface de rede.
* **Fluxo de Rede**: O pacote *DHCP Discover* transita pelo switch `SW-CT09`, passa pelo tronco de fibra monomodo até o `SW-CT12`, atinge a subinterface `g0/0.30` do Cisco 2911, onde é convertido em unicast via `ip helper-address 192.168.20.30` e entregue ao `SRV-DHCP`.
* **Resultado**: *DHCP request successful* com IP atribuído na faixa `192.168.30.0/24`, máscara `255.255.255.0`, gateway `192.168.30.1` e DNS `8.8.8.8`.
* **Status**: **Aprovado**.
