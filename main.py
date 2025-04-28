from bot import responder


def iniciar_chat():
    print("🤖 Chatbot: Olá! Digite sua mensagem ou 'sair' para encerrar a conversa.")
    while True:
        msg = input("Você: ").strip()

        if not msg:
            print("🤖 Chatbot: Você não digitou nada! Tente enviar uma mensagem.")
            continue

        if msg.lower() in ["sair", "exit"]:
            print("🤖 Chatbot: Até logo! 👋")
            break

        resposta = responder(msg)
        print(f"🤖 Chatbot: {resposta}")


if __name__ == "__main__":
    iniciar_chat()