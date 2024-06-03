import tkinter as tk
from tkinter import scrolledtext
from chatbot import chatbot_response
from model_training import load_data, train_model
from preprocessing import preprocess_text

# Função para obter a resposta do chatbot
def get_response():
    user_input = user_entry.get()
    response = chatbot_response(user_input)
    chat_display.insert(tk.END, "Você: " + user_input + "\n")
    chat_display.insert(tk.END, "Bot: " + response + "\n")
    user_entry.delete(0, tk.END)

# Carregar a base de dados
df = load_data('data/test.csv')

# Aplicar o pré-processamento ao campo 'text'
df['processed_text'] = df['text'].apply(preprocess_text)

# Treinar o modelo
model, vectorizer = train_model(df)

# Configurar a janela principal
root = tk.Tk()
root.title("Chatbot")

# Área de exibição de conversa
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_display.pack(padx=20, pady=20)

# Campo de entrada do usuário
user_entry = tk.Entry(root, width=100)
user_entry.pack(padx=20, pady=5)

# Botão de enviar
send_button = tk.Button(root, text="Enviar", command=get_response)
send_button.pack(padx=20, pady=5)

# Iniciar a aplicação
root.mainloop()
