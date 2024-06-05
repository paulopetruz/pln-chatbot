import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Baixar recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Verificar se a entrada é uma string
    if not isinstance(text, str):
        return ''
    # Remover URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Remover menções e hashtags
    text = re.sub(r'\@\w+|\#','', text)
    # Converter para minúsculas
    text = text.lower()
    # Remover pontuação
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenizar o texto
    tokens = word_tokenize(text)
    # Remover stop words
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Lematizar palavras
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    # Juntar tokens de volta em uma string
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text