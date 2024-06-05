import tkinter as tk
from model_training import load_data, train_model
from preprocessing import preprocess_text
from model_training import train_model
from interface import ChatbotInterface

# Carregar a base de dados
df = load_data('data/test.csv')

# Verificar se a coluna 'text' contém NaN e substituí-los por strings vazias
df['text'] = df['text'].fillna('')

# Aplicar a função de preprocessamento na coluna 'text'
df['processed_text'] = df['text'].apply(preprocess_text)

# Tratar valores NaN na coluna 'sentiment'
# Aqui, estamos removendo as linhas onde 'sentiment' é NaN
df = df.dropna(subset=['sentiment'])

# Treinar o modelo
model, vectorizer = train_model(df)

# Iniciar interface do chatbot
chatbot_interface = ChatbotInterface(model, vectorizer)
chatbot_interface.run()
