# ==============================================================================
# # 6_condicionales -> 6_buenas_practicas.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 8: BUENAS PRÁCTICAS Y CLÁUSULAS DE GUARDA (10 Minutos)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 8.1 El Problema: Código Espagueti Anidado (Pésima práctica)
# ------------------------------------------------------------------------------
# ? Variables de control de acceso al gimnasio
tiene_membresia = True
trae_calzado_deportivo = False

print("--- Ejecutando Enfoque Incorrecto (Anidado) ---")

# * ❌ ENFOQUE INCORRECTO: Observa cómo el código se va hacia la derecha y se vuelve confuso
if tiene_membresia:
    if trae_calzado_deportivo:
        print("Acceso concedido. ¡Disfruta tu entrenamiento!")
    else:
        print("Error: Por seguridad, no puedes ingresar sin tenis deportivos.")
else:
    print("Error: Tu membresía expiró o no está registrada en el sistema.")


# ------------------------------------------------------------------------------
# * 8.2 La Solución: Cláusulas de Guarda (Código Profesional y Plano)
# ------------------------------------------------------------------------------
# ? Mismo problema, pero descartando los errores de forma inmediata al inicio
print("\n--- Enfoque Profesional (Cláusulas de Guarda) ---")

# * 1. Descartamos el primer error de forma directa
if not tiene_membresia:
    print("Error: Tu membresía expiró o no está registrada en el sistema.")
    # ! Nota para el profesor: En una función real, aquí usaríamos un 'return' para cortar la ejecución.

# * 2. Descartamos el segundo error de forma directa
if not trae_calzado_deportivo:
    print("Error: Por seguridad, no puedes ingresar sin tenis deportivos.")

# * 3. El "Camino Feliz" (Éxito) queda completamente libre de anidaciones
if tiene_membresia and trae_calzado_deportivo:
    print("Acceso concedido. ¡Disfruta tu entrenamiento!")


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: El peligro del operador 'in' con minúsculas mezcladas
# ? Recuerda que la búsqueda es Case Sensitive. Si buscas un texto, hazlo con la caja correcta.
alerta_radar = "Se detectó un dron no autorizado en el sector norte."
print("¿'dron' (minúscula) está?:", "dron" in alerta_radar)
print("¿'Dron' (mayúscula) está?:", "Dron" in alerta_radar)
print("Solución Inteligente usando .lower():", "dron" in alerta_radar.lower())

# * Ejemplo B: El impacto de .count() en textos que no contienen la palabra
# ? Si buscas un elemento que está ausente, .count() nunca lanzará un error; simplemente devolverá 0.
registro_asistencias = "Carlos, Ana, Sofía"
print("Conteo de 'Pedro' en el registro:", registro_asistencias.count("Pedro"))

# * Ejemplo C: El uso de .split() para contar palabras exactas en una frase
# ? Combinando .split() con len(), puedes contar cuántas palabras componen un texto de manera exacta.
slogan_gimnasio = "Fuerza disciplina y constancia"
palabras_separadas = slogan_gimnasio.split()
print(f"El slogan tiene exactamente {len(palabras_separadas)} palabras individuales.")
