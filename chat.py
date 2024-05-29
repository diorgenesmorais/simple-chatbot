import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def chat_with_bot():
    chat = model.start_chat(history=[])
    print('Chatbot: Olá! Como posso te ajudar hoje?')
    while True:
        user_input = input('Você: ')
        if user_input.lower() == 'sair':
            print('Chatbot: Até mais!')
            break
        respose = chat.send_message(user_input)
        print('Chatbot:\n', respose.text)

if __name__ == "__main__":
    chat_with_bot()

