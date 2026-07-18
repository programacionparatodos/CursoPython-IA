# 1. pip --version
# 2. pip install groq
# 3. Obtener la API Key (console.groq.com)# 
# API KEY: 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

from groq import Groq

cliente = Groq(api_key='GROQ_API_KEY')

response = cliente.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages = [
        {
            "role": "user",
            "content": "Explícame en una sola fila que es una API"
        }
    ]
)

respuesta_texto = response.choices[0].message.content

print(respuesta_texto)