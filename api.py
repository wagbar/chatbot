# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from bot import responder

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.post("/mensagem")
def responder_mensagem(msg: Mensagem):
    resposta = responder(msg.texto)
    return {"resposta": resposta}

@app.get("/")
def home():
    return {"mensagem": "API do Chatbot está no ar 🚀"}