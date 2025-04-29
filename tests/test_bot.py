import unittest
from bot import responder, normalizar_texto

class TestChatbot(unittest.TestCase):
    def test_normalizar_texto_ola(self):
        self.assertEqual(normalizar_texto("Olá"), "ola")

    def test_normalizar_texto_com_acentos(self):
        self.assertEqual(normalizar_texto("Você!"), "voce")

    def test_responder_oi(self):
        self.assertEqual(responder("oi"), "Olá! Como posso ajudar?")

    def test_responder_ajuda(self):
        self.assertEqual(responder("ajuda"), "Claro! Você pode perguntar sobre comandos como 'oi', 'tchau', 'ajuda'...")

    def test_responder_mensagem_desconhecida(self):
        self.assertEqual(responder("abcdefg"), "Desculpe, não entendi o que você quis dizer.")

if __name__ == '__main__':
    unittest.main()