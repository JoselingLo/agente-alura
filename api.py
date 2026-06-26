from fastapi import FastAPI
from loader import cargar_datos
from agent import responder_pregunta

app = FastAPI()

df = cargar_datos("data/ventas.csv")

@app.get("/")
def home():
    return {"mensaje": "Agente IA funcionando"}

@app.get("/preguntar")
def preguntar(q: str):
    respuesta = responder_pregunta(df, q)
    return {
        "pregunta": q,
        "respuesta": respuesta
    }