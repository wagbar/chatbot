from bot import responder, normalizar_texto

def test_normalizar_texto_ola():
    assert normalizar_texto("Olá") == "ola"

def test_normalizar_texto_com_acentos():
    assert normalizar_texto("Você!") == "voce"

def test_responder_oi():
    assert responder("oi") == "Olá! Como posso ajudar?"

def test_responder_ajuda():
    assert responder("ajuda") == "Claro! Você pode perguntar sobre comandos como 'oi', 'tchau', 'ajuda'..."

def test_responder_mensagem_desconhecida():
    assert responder("abcdefg") == "Desculpe, não entendi o que você quis dizer."