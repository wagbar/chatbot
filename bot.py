import unicodedata
from datetime import datetime

def normalizar_texto(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def responder(mensagem):
    mensagem = normalizar_texto(mensagem).strip()

    if "tempo" in mensagem:
        return "Não sei a previsão do tempo agora, mas espero que esteja um dia lindo!"

    if "hora" in mensagem or "horas" in mensagem:
        agora = datetime.now()
        return f"Agora são {agora.strftime('%H:%M')}."

    respostas = {
        "oi": "Olá! Como posso ajudar você hoje?",
        "ola": "Oi! Tudo certo por aí?",
        "bom dia": "Bom dia! Não esqueça de se hidratar! 💧",
        "boa tarde": "Boa tarde! Como posso te ajudar?",
        "boa noite": "Boa noite! Espero que tenha tido um ótimo dia!",
        "tudo bem": "Tudo ótimo, obrigado por perguntar!",
        "qual seu nome": "Sou um chatbot em constante evolução!",
        "ajuda": "Claro! Você pode me perguntar sobre o tempo, a hora, ou apenas dizer 'oi'.",
        "tchau": "Até mais! Foi ótimo conversar com você!",
    }

    # Tenta achar uma resposta conhecida
    resposta = respostas.get(mensagem)

    # Se não encontrar, retorna uma resposta padrão
    if resposta is None:
        resposta = "Desculpe, não entendi o que você quis dizer. Pode tentar de outra forma?"

    return resposta