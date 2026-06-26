from loader import cargar_datos
from agent import responder_pregunta

df = cargar_datos("data/ventas.csv")

print("🤖 Agente listo. Escribe 'salir' para terminar")

while True:
    pregunta = input("👉 ")

    if pregunta.lower() == "salir":
        break

    respuesta = responder_pregunta(df, pregunta)
    print("\n🤖", respuesta, "\n")