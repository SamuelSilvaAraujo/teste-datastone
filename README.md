## Explicação do sistema

O sistema utiliza o Framework Django e Django Rest, criando uma api simples onde recebe um valor e as moedas que você deseja converter, é divido em dois aplicativos onde o aplicativo CORE funciona como frontend e API tem o sistema de conversão das moedas utilizando o django rest framework para receber os dados.

## Rodando a aplicação

### Docker

Você precisa ter o [Docker](https://docs.docker.com/engine/install/) e [Docker Compose](https://docs.docker.com/compose/install/) instalado.

#### Iniciando a aplicação

```
docker-compose up --build datastone
```

Após iniciado o container, a aplicação estará disponível em `http://localhost:8000`.
