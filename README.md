# 🤖 Agente IA para análisis de ventas

Este proyecto es un agente de inteligencia artificial que permite responder preguntas sobre un conjunto de datos de ventas utilizando Python.

---

## 📌 Descripción

El sistema carga un archivo CSV con datos de ventas y permite consultar información mediante lenguaje natural, como:

- ¿Cuál fue el producto más vendido?
- ¿Cuántas ventas tuvo un producto en un mes específico?

---

## 🧠 Tecnologías utilizadas

- Python
- Pandas
- LangChain
- OpenAI (opcional)
- Git & GitHub

---

## 📁 Estructura del proyecto

agente-alura/
│
├── data/
│   └── ventas.csv
│
├── app.py
├── agent.py
├── loader.py
├── requirements.txt
├── README.md

---

## ▶️ Cómo ejecutar el proyecto

1. Instalar dependencias:

```bash
pip install pandas langchain langchain-openai openai
## ☁️ Deploy en Render

Este proyecto fue desplegado en Render como una API pública.

🔗 Link:
https://agente-alura.onrender.com
## 🌐 Deploy en la nube

La aplicación fue desplegada correctamente en Render y está disponible públicamente.

🔗 URL del proyecto:
https://agente-alura.onrender.com

## 🚀 Cómo probar el agente

Puedes hacer consultas directamente desde el navegador, por ejemplo:

https://agente-alura.onrender.com/preguntar?q=¿Cuál fue el producto más vendido?

El sistema responderá usando los datos del archivo CSV.