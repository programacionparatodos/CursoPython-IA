# ==============================================================================
# # 6_condicionales -> 3_condicional_anidada.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 5: LA CONDICIONAL ANIDADA
# ==============================================================================

# ------------------------------------------------------------------------------
# * 5.1 Enfoque Tradicional Complejo (Anidación Manual con else: if)
# ------------------------------------------------------------------------------
# ? Evaluamos el gasto del comensal para calcular su nivel de beneficio
total_consumo = 350

print("--- Ejecutando Enfoque Complejo (else: if) ---")

# * Observa cómo el código se va desplazando peligrosamente hacia la derecha
if total_consumo >= 500:
    print("¡Nivel Oro! Recibe un postre gratis.")
else:
    if total_consumo >= 200:
        print("¡Nivel Plata! Recibe un café gratis.")
    else:
        print("Nivel Bronce. Gracias por su visita.")


# ------------------------------------------------------------------------------
# * 5.2 Enfoque Optimizado Moderno (Uso de ELIF)
# ------------------------------------------------------------------------------
# ? Mismo problema, pero estructurado de forma lineal y legible gracias a elif
print("\n--- Ejecutando Enfoque Optimizado (elif) ---")

if total_consumo >= 500:
    print("¡Nivel Oro! Recibe un postre gratis.")
elif total_consumo >= 200:
    print("¡Nivel Plata! Recibe un café gratis.")
else:
    print("Nivel Bronce. Gracias por su visita.")

# TODO: Ver como el 'elif' elimina los escalones de sangría del código anterior.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: El orden de los factores sí altera el producto en un ELIF
# ? Python evalúa de arriba a abajo. Si colocas una condición muy general al principio,
# ? las condiciones más específicas de abajo quedarán "atrapadas" y nunca se ejecutarán.
# ? Caso: Sistema de propinas automáticas en la cafetería.
monto_cuenta = 600

print("--- ❌ Orden Incorrecto (Error de Lógica) ---")
if monto_cuenta >= 100:
    print("Aplicando 10% de propina sugerida (Nivel Básico).") # ! Se detiene aquí porque 600 >= 100 es True
elif monto_cuenta >= 500:
    print("Aplicando 15% de propina sugerida (Nivel Premium).") # ❌ Este bloque se vuelve código muerto

print("\n--- ✅ Orden Correcto (De lo más específico a lo más general) ---")
if monto_cuenta >= 500:
    print("Aplicando 15% de propina sugerida (Nivel Premium).") # ⭐ Se ejecuta este bloque correctamente
elif monto_cuenta >= 100:
    print("Aplicando 10% de propina sugerida (Nivel Básico).")

# * Ejemplo B: Combinando ELIF con validación de tipos de datos (.isdigit)
# ? Imagina que el sistema lee el código de un combo de desayuno. El cliente puede escribir
# ? el número del combo o presionar ENTER. Evitamos que el programa falle mezclando lógica.
seleccion_usuario = "3" # Simula la entrada de la botonera

print("\n--- Procesando Selección de Menú ---")
if seleccion_usuario == "":
    print("Notificación: No seleccionaste nada. Te asignamos el Combo del Día: Café Negro.")
elif seleccion_usuario.isdigit():
    num_combo = int(seleccion_usuario)
    if num_combo == 1:
        print("Combo 1: Capuccino + Facturas.")
    elif num_combo == 2:
        print("Combo 2: Expresso + Tostado.")
    else:
        print(f"El número {num_combo} no está en nuestro menú. Elige del 1 al 2.")
else:
    print("Error: Entrada no válida. Por favor, usa números enteros para elegir.")

# * Ejemplo C: El uso de ELIF sin un bloque ELSE final
# ? El bloque 'else' no es obligatorio al final de un 'elif'. Si ninguna condición se cumple
# ? y no hay 'else', Python simplemente continúa con la ejecución del resto del script.
# ? Caso: Validar cupones de descuento específicos de temporada.
cupón_descuento = "INVIERNO"

if cupón_descuento == "PRIMAVERA":
    descuento = 15
elif cupón_descuento == "VERANO":
    descuento = 20
# ! Nota que no pusimos un else. Si el cupón es "INVIERNO", no pasa nada, se ignora la estructura.

print("\nValidación de cupones terminada.")