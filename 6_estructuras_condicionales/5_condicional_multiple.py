# ==============================================================================
# # 6_condicionales -> 5_condicional_multiple.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 7: CONDICIONAL MÚLTIPLE - MATCH CASE
# ==============================================================================

# ------------------------------------------------------------------------------
# * 7.1 Reemplazo Estructurado del Switch-Case Tradicional
# ------------------------------------------------------------------------------
# ? El cliente interactúa con una pantalla táctil para buscar su juego favorito
plataforma_elegida = "PlayStation"

print("Buscando ubicación en la tienda...")

# * Evaluamos de forma directa la variable contra patrones exactos
match plataforma_elegida:
    case "PlayStation":
        print("Ubicación: Dirígete al Pasillo A (Zona Sony).")
    case "Xbox":
        print("Ubicación: Dirígete al Pasillo B (Zona Microsoft).")
    case "Nintendo":
        print("Ubicación: Dirígete al Pasillo C (Zona Nintendo).")
    case "PC":
        print("Ubicación: Dirígete al Pasillo Central (Componentes y Códigos).")
    case _:
        # * Este bloque atrapa cualquier texto que no coincida con los anteriores
        print("Ubicación: Plataforma no reconocida. Consulta en el mostrador principal.")

# ! NOTA: 'match-case' es mucho más rápido de leer que escribir 5 bloques 'elif' seguidos.
# TODO: Esta característica requiere obligatoriamente Python 3.10 o superior.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: El uso de condicionales internas en un caso (Guards en match-case)
# ? ¡DATO CURIOSO AVANZADO! Dentro de un 'case', puedes agregar un 'if' secundario. 
# ? Esto se conoce como una "guarda" y sirve para filtrar aún más la opción.
# ? Caso: El cliente compra un juego, pero el precio varía si tiene un cupón de descuento.
categoria_juego = "Retro"
tiene_cupon = True

print("--- Procesando precio con Guarda (if) en match-case ---")
match categoria_juego:
    # * Este caso SOLO se ejecuta si la categoría es Retro Y además tiene_cupon es True
    case "Retro" if tiene_cupon:
        print("Precio Especial: $5 (Descuento por cupón retro aplicado).")
    case "Retro":
        print("Precio Estándar: $15.")
    case _:
        print("Precio Estándar: $60 (Estreno).")

# * Ejemplo B: Capturando el valor dentro del caso comodín (Variable Capture)
# ? En lugar de usar el guion bajo (_) que borra el dato, puedes inventar un nombre de variable 
# ? en el último caso para atrapar el texto desconocido y usarlo en el mensaje de error.
metodo_pago_ingresado = "Criptomonedas"

print("\n--- Validando método de pago en la caja registradora ---")
match metodo_pago_ingresado:
    case "Efectivo":
        print("Abriendo caja física del local.")
    case "Tarjeta":
        print("Encendiendo terminal de punto de venta.")
    case metodo_desconocido:
        # * 'metodo_desconocido' atrapa el texto "Criptomonedas" de forma automática
        print(f"Error: El método '{metodo_desconocido}' no está integrado en la tienda.")

# * Ejemplo C: El comportamiento de match-case con tipos de datos diferentes
# ? 'match-case' hace una comparación estricta de valor y tipo. 1 no es lo mismo que "1".
# ? Caso: El usuario presiona el botón físico de la consola de videojuegos.
codigo_boton = "1" # El sensor mandó un texto en lugar de un número entero

print("\n--- Diagnóstico de la Botonera ---")
match codigo_boton:
    case 1:
        print("Acción: Encender la consola.")
    case 2:
        print("Acción: Reiniciar sistema.")
    case _:
        # * Cae aquí porque "1" (String) NO es igual a 1 (Entero)
        print("Alerta: Entrada de datos corrupta o botón no asignado.")