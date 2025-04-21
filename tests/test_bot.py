from bot import responder

def test_resposta_oi():
    assert responder("oi") == "Olá! Como posso ajudar?"

def test_resposta_desconhecida():
    assert responder("qual é a sua idade?") == "Eu não tenho uma idade definida porque sou um robô"