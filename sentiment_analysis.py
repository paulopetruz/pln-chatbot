import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Baixar o lexicon necessário do NLTK
nltk.download('vader_lexicon')

# Inicializar o analisador de sentimentos
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'
