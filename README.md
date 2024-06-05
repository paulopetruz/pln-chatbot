**# Projeto final: Desenvolvimento de Chatbot com Análise de Sentimento**

# Chatbot com Análise de Sentimentos

Este projeto desenvolve um chatbot capaz de interagir com usuários, compreendendo e respondendo a mensagens de forma contextualmente relevante, utilizando técnicas de processamento de linguagem natural (NLP) com ênfase na análise de sentimentos.

## Objetivo

- Desenvolver um chatbot que possa fornecer respostas contextualmente relevantes.
- Implementar a análise de sentimentos para entender a polaridade emocional das mensagens dos usuários.

## Funcionalidades

- Processamento de texto: remoção de URLs, menções, hashtags, pontuação e conversão para minúsculas.
- Tokenização, remoção de stop words e lematização.
- Análise de sentimentos usando NLTK.
- Interface gráfica de usuário (GUI) usando Tkinter.

## Base de dados utilizada no treinamento
- Sentimentos do Twitter pelo mundo

## Requisitos

- Python 3.x
- Bibliotecas Python: pandas, nltk, scikit-learn, tk

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/paulopetruz/pln-chatbot
    cd pln-chatbot
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque seu arquivo CSV com dados no diretório principal do projeto.
2. Execute o script principal:
    ```bash
    python main.py
    ```

3. Interaja com o chatbot através da interface gráfica que será aberta.

## Estrutura do Projeto
- `main.py`: Script principal para execução do chatbot.
- `preprocessing.py`: Funções de pré-processamento de texto.
- `model_training.py`: Funções para treinamento do modelo de análise de sentimentos.
- `interface.py`: Código da interface gráfica com Tkinter.
- `requirements.txt`: Lista de dependências do projeto.