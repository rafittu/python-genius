# 🎨 Genius

###

<br>

O projeto **Genius** é um sistema que prevê a próxima cor e sequência de cores em padrões similares ao clássico jogo **Genius**!

Utilizando redes neurais e aprendizado incremental em tempo real, o sistema aprende continuamente a partir de sequências de cores geradas dinamicamente, proporcionando uma experiência única de predição baseada em cores.

<br>

## Tecnologias

Este projeto utiliza as seguintes tecnologias:

- **Python** como linguagem principal;
- **SQLAlchemy ORM** para integração com o banco de dados **PostgreSQL**;
- **Flask** para construção de uma aplicação web responsiva;
- **Socket.IO** para comunicação em tempo real entre o servidor e o cliente;
- **TensorFlow** para criação e treinamento de uma rede neural do tipo **LSTM (Long Short-Term Memory)**, 
- **Docker** como uma ferramenta de containerização;

<br>

## Arquitetura do Sistema

A rede neural LSTM é configurada para realizar **aprendizado incremental**, processando novas entradas de dados continuamente. A cada nova cor recebida, o modelo é atualizado com o histórico e re-treinado, garantindo que a predição de padrões e sequência de cores se torne mais precisa à medida que o sistema evolui.

O banco de dados registra as cores em suas respectivas componentes RGB, assim como o `timestamp` de cada entrada, facilitando a análise e o processamento dos dados em tempo real.

<br>

## Configuração do Projeto

### Requisitos para rodar a aplicação

- Python (versão 3.11 ou superior)
- Docker e Docker Compose;
 
 ### Instalação

1. Clonando o repositório:

```bash
$ git clone git@github.com:rafittu/python-genius.git
$ cd python-genius
```

2. Crie um arquivo `.env` na raiz do projeto e preencha as informações de acordo com o arquivo `.env.example` disponível.

3. Inicie o ambiente de desenvolvimento:

```bash
$ docker-compose up --build
```

<br>

##

<p align="right">
  <a href="https://www.linkedin.com/in/rafittu/">Rafael Ribeiro 🚀</a>
</p>
