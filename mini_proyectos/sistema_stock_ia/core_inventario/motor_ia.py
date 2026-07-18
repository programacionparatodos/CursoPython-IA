from groq import Groq

cliente = Groq(api_key='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')

def predecir_demanda_futura(historial_ventas):
    if not historial_ventas:
        return 0
    
    historial_texto = str(historial_ventas)

    try:
        response = cliente.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en logística de inventarios. Tu única tarea es analizar listas de ventas diarias asadas y predecir el número entero de ventas para el día de mañana. Responde ÚNICAMENTE con el número entero, sin textos ni explicaciones."
                },
                {
                    "role": "user",
                    "content": f"Este es el historial de unidades vendidas recientemente de mi producto: {historial_texto}. ¿Cuántas unidades se venderán mañana?"
                }      
            ],
            temperature = 0.2
        )

        respuesta_texto = response.choices[0].message.content.strip()

        return int(respuesta_texto)
    
    except Exception:
        suma_ventas = 0
        for venta in historial_ventas:
            suma_ventas += venta
        
        return int(suma_ventas / len(historial_ventas))
