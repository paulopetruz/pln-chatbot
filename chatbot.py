from preprocessing import preprocess_text
from sentiment_analysis import analyze_sentiment

def chatbot_response(user_input):
    # Pré-processar a entrada do usuário
    processed_input = preprocess_text(user_input)
    # Analisar o sentimento da entrada
    sentiment = analyze_sentiment(processed_input)
    # Lógica de resposta baseada no sentimento
    if sentiment == 'positive':
        response = "Que ótimo! Como posso ajudar mais?"
    elif sentiment == 'negative':
        response = "Sinto muito que você esteja se sentindo assim. Em que posso ajudar?"
    else:
        response = "Entendo. Em que mais posso ajudar?"
    return response
