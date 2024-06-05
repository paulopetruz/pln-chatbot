from preprocessing import preprocess_text
from sentiment_analysis import analyze_sentiment

def chatbot_response(user_input):
    # Pré-processar a entrada do usuário
    processed_input = preprocess_text(user_input)
    # Analisar o sentimento da entrada
    sentiment = analyze_sentiment(processed_input)
    # Lógica de resposta baseada no sentimento
    if sentiment == 'positive':
        response = "Eita como tá feliz, me passa um pouco dessa sua felicidade"
    elif sentiment == 'negative':
        response = "Ih rapaz, parece que você ativou o meu sentido de confusão!"
    else:
        response = "Hmm, sem grandes surpresas aqui. Continue balançando pelas ruas da cidade!"
    return response
