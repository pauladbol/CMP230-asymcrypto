## Setup

#### Criar um virtual environment:

``python3 -m venv /path/to/new/virtual/env``


#### Instalar dependencias:

``pip install -r requirements.txt``



## RSA

#### Rodar:

``python rsa.py``

#### Escolha entre as opções:

1: "Gerar chaves RSA"

2: "Encriptar mensagem"

3: "Decriptar mensagem"


## Diffie-Hellman/Transmissão de chaves


#### Rodar em diferentes janelas do terminal:

``python tcp_server.py``

``python tcp_client.py``


#### Escolher entre as opções:

1: "Gerar q"

2: "Gerar a"

3: "Gerar chave pública"

4: "Gerar chave simétrica"

5: "Enviar mensagem"

6: "Receber mensagem"

7: "Sair"


## Passos para simular acordo/geração de chaves:

- Gerar par de chaves para usuário 1 através do ``rsa.py``
- Gerar par de chaves para usuário 2 através do ``rsa.py``

##### Usuário 1 (ex.: cliente):

- Gerar ``q`` utilizando chave privada
- Enviar ``q`` gerado para usuário 2


##### Usuário 2 (ex.: servidor):
- Receber mensagem
- Gerar ``q`` utilizando a chave privada e como base ``q`` o valor já proposto pelo usuário 1
- Enviar ``q`` gerado para usuário 1

##### Usuário 1:
- Receber mensagem
- Gerar ``a`` com base no ``q`` recebido
- Enviar ``a`` para usuário 2

##### Usuário 2:
- Receber mensagem
- Gerar chave pública com base na própria chave privada, ``q`` e ``a`` acordados
- Enviar chave pública para usuário 1

##### Usuário 1:
- Receber mensagem
- Gerar chave pública com base na própria chave privada, ``q`` e ``a`` acordados
- Enviar chave pública para usuário 2

##### Usuário 2:
- Receber mensagem
- Gerar chave simétrica com base na chave pública recebida do usuário 2, a própria chave privada e ``q`` 

##### Usuário 1:
- Gerar chave simétrica com base na chave pública recebida do usuário 2, a própria chave privada e ``q`` 
