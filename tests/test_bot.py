from bot import responder

def test_resposta_oi():
    assert responder("oi") == "Olá! Como posso ajudar?"

def test_resposta_desconhecida():
    assert responder("qual é a sua idade?") == "Desculpe, não entendi o que você quis dizer."