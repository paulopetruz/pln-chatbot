**# Projeto final: Desenvolvimento de Chatbot com Análise de Sentimento**

 

**## Objetivo:**

Desenvolver um chatbot capaz de interagir com usuários, compreendendo e respondendo a mensagens de forma contextualmente relevante, utilizando técnicas de processamento de linguagem natural, com ênfase na análise de sentimentos.

 

## Etapas do Projeto:

1. **Definição do Escopo** 

Identificar o propósito do chatbot (por exemplo, suporte ao cliente, assistente pessoal, repositório de informação, entretenimento, etc.).

2. **Coleta de Dados**

A base conterá conhecimento para o chatbot referente ao assunto definido na etapa 1.

3. **Pré-processamento e Análise de Sentimento**

Implementação de técnicas de pré-processamento de texto (para melhorar a correspondência entre a entrada do usuário e as frases contidas na base de conhecimento).

Integração de um módulo de análise de sentimento (NLTK ou TF-IDF) para entender a polaridade emocional de novas mensagens entradas pelo usuário.

Se o modelo escolhido for por NLTK, basta usar as funções da biblioteca. Se for TF-IDF, há a necessidade de desenvolver uma árvore e, para isso, utilizaremos uma nova base de conhecimento com as possíveis frases de entrada analisadas quanto ao seu sentimento (pode desenvolver ou buscar no kaggle).

4. **Treinamento do Modelo de Linguagem (só para a TF-IDF)**

Treinamento do modelo (árvore) utilizando os dados coletados (para o caso do TF-IDF).

5. **Integração da Análise de Sentimento no Chatbot**

Os alunos integram o módulo de análise de sentimento no fluxo de processamento do chatbot.

Desenvolvimento de lógica para ajustar respostas com base na análise de sentimento.

6. **Desenvolvimento da Interface de Usuário**

TKinter - python

interfaces em python - não usar o Colab (IDLE, pyCharm, outros…)

Implementação de uma interface de usuário amigável para interação com o chatbot.

Considerar a possibilidade do usuário ajustar o humor das respostas do Chatbot (a mais)

7. **Testes e Avaliação**

Testes do chatbot em diferentes cenários.

Avaliação da eficácia da análise de sentimento em relação às respostas geradas.

8. **Otimização e Ajustes**

Ajustes no modelo e na lógica do chatbot com base nos resultados dos testes.

Otimização da performance e eficiência.

9. **Apresentação Final**

Apresentação do chatbot em funcionamento, destacando os recursos de análise de sentimento e interatividade.

Discussão sobre desafios enfrentados, lições aprendidas e eficiência do modelo

