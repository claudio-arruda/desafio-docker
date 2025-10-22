# Desafio1-Docker

Executar uma chamada via HTTP com método GET a plicação irá listar os arquivos de um diretório

# Características

* Listar todos os arquivos do diretório mapeado
* Retornar um arquivo por linha via HTTP GET
* Rodar na porta 8000
* Funcionar com qualquer diretório do host mapeado para /files_data no container

# Pré-requisitos

Docker instalado na sua máquina

# Como Usar

Opção 1: Build local
(Build da imagem)

docker build -t desafiodocker .

Opção 2: Run local
(Executar o container)

docker run -it -d --name desafio_docker -v $PWD/files_data:/files_data -p 8000:8000 desafiodocker:latest

Opção 3: Listar arquivos
(Executar o comando curl no prompt do linux)

curl http://127.0.0.1:8000/

# Estrutura do Projeto

├── app.py
├── Dockerfile
├── files_data
│   ├── files01
│   ├── files02
│   ├── files03
│   └── files04
└── requirements.txt

# Monitoramento

Monitorar recursos do container:

* docker stats desafio_docker

Verificar logs do container:

* docker logs --tail=50 -f desafio_docker

Caso precise fazer alguma chamada via HTTP dentro de um ckluster kubernetes via Liveness Probes, foi criado um health check:

* curl http://localhost:8000/health
