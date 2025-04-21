from bot import responder

def iniciar_chat():
    print("🤖 Chatbot: Olá! Digite sua mensagem ou 'sair' para encerrar.")
    while True:
        msg = input("Você: ")
        if msg.lower() in ["sair", "exit"]:
            print("🤖 Chatbot: Até logo!")
            break
        resposta = responder(msg)
        print(f"🤖 Chatbot: {resposta}")

if __name__ == "__main__":
    iniciar_chat()