from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/teste")
def hello_world():
    return {"mensagem": "Deu certo"}


# Criando um endpoint para receber dois números e retornar a soma
@app.post("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2    
    return {"resultado": total}


# Formato 2: recebendo os números no corpor da requisição
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


class Numero(BaseModel):
    numero1: int
    numero2: int
    numero3: int = 0

@app.post("/soma_formato3")
def soma_formato3(numero: Numero):
    total = numero.numero1 + numero.numero2 + numero.numero3
    return {"resultado": total}


    