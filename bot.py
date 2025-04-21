import unicodedata

def normalizar_texto(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def responder(mensagem):
    mensagem = mensagem.lower()

    respostas = {
        "oi": "Olá! Como posso ajudar?",
        "olá": "Oi! Tudo bem por aí?",
        "bom dia": "Bom dia! Já tomou água hoje?",
        "tudo bem": "Que bom! Comigo também está tudo certo.",
        "tchau": "Até logo! Foi bom conversar com você.",
        "ajuda": "Claro! Você pode perguntar sobre comandos como 'oi', 'tchau', 'ajuda'..."
    }

    return respostas.get(mensagem, "Desculpe, não entendi o que você quis dizer.")