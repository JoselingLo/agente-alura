def responder_pregunta(df, pregunta):

    pregunta = pregunta.lower()

    # 🔥 PRODUCTO MÁS VENDIDO
    if "más vendido" in pregunta or "mas vendido" in pregunta:
        resultado = df.groupby("producto")["ventas"].sum().idxmax()
        total = df.groupby("producto")["ventas"].sum().max()

        return f"El producto más vendido es {resultado} con {total} unidades."

    # 🔥 VENTAS POR PRODUCTO
    for producto in df["producto"].unique():
        if producto.lower() in pregunta:
            total = df[df["producto"] == producto]["ventas"].sum()
            return f"El producto {producto} vendió un total de {total} unidades."

    return "No encontré una respuesta en los datos."