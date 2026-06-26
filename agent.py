def responder_pregunta(df, pregunta):
    datos = df.to_string(index=False)

    return f"""
🤖 (Modo demo sin IA real)

Recibí tu pregunta:
"{pregunta}"

Datos disponibles:
{datos}

👉 Respuesta simulada:
El sistema encontró información en el dataset y procesó la consulta correctamente.
"""