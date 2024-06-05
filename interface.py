import tkinter as tk
from tkinter import scrolledtext, Label
from preprocessing import preprocess_text
from chatbot import chatbot_response
from PIL import Image, ImageTk

class ChatbotInterface:
    def __init__(self, model, vectorizer):
        # Inicialização da interface
        self.model = model
        self.vectorizer = vectorizer
        self.window = tk.Tk()
        self.window.title("Chatbot") 

        # Carregar e exibir o avatar
        avatar_image = Image.open("asset/umiranha.png")
        avatar_image = avatar_image.resize((100, 100), Image.FIXED)
        avatar_photo = ImageTk.PhotoImage(avatar_image)
        self.avatar_label = Label(self.window, image=avatar_photo)
        self.avatar_label.image = avatar_photo
        self.avatar_label.pack(side="left")

        # área de exibição das mensagens
        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=20, pady=10)
        self.send_initial_message()

        # Entrada de texto para o usuário
        self.entry = tk.Entry(self.window, width=80)
        self.entry.pack(padx=20, pady=10)
        self.entry.bind("<Return>", self.send_message)

    def send_initial_message(self):
        initial_message = "Oi, sou humiranha\n Como você se sente?\n"
        self.display_message(initial_message)

    def send_message(self, event):
        # Método para enviar mensagem quando o usuário pressiona Enter
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.display_message(f"You: {user_input}\n")
        self.get_response(user_input)

    def display_message(self, message):
        # Método para exibir mensagens na área de chat
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message)
        self.chat_area.configure(state='disabled')

    def get_response(self, user_input):
        # obter a resposta do chat
        processed_input = preprocess_text(user_input)
        vectorized_input = self.vectorizer.transform([processed_input])
        sentiment = self.model.predict(vectorized_input)[0]
        response = chatbot_response(sentiment)
        self.display_message(f"Umiranha ({sentiment}): {response}\n")

    def run(self):
        self.window.mainloop()
