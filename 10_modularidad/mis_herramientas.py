# ==============================================================================
# # 10_modularidad -> mis_herramientas.py
# ==============================================================================

def tam(coleccion):
    contador = 0
    for elemento in coleccion:
        contador = contador + 1
    return contador # Retorna un tipo de dato: int

def calcular_promedio(lista_numeros):
    suma_total = sum(lista_numeros)
    cantidad_elementos = tam(lista_numeros) # Invocamos nuestra función de arriba
    
    if cantidad_elementos == 0:
        return 0.0
    return suma_total / cantidad_elementos # Retorna un tipo de dato: float

# ==============================================================================
# * EL ESCUDO DE SEGURIDAD MÁS OBLIGATORIO DE PYTHON (`__main__`)
# ==============================================================================

if __name__ == "__main__":
    print("--- 🛠️ MODO DESARROLLADOR: Probando herramientas aritméticas ---")
    # * Esto solo se leerá si das 'Play' DIRECTAMENTE a este archivo secundario
    lista_prueba = [10, 20, 30]
    print(f"[TEST] Tamaño calculado por nuestra función tam(): {tam(lista_prueba)}")
    print(f"[TEST] Promedio calculado: {calcular_promedio(lista_prueba)}")