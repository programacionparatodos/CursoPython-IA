# ==============================================================================
# # 6_condicionales -> 6_buenas_practicas.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 8: BUENAS PRÁCTICAS Y CLÁUSULAS DE GUARDA (10 Minutos)
# ==============================================================================

"""
[GUION PARA EL PROFESOR — CRONÓMETRO: MINUTO 50 A 60]
• El peligro del código Espagueti: "Cuando metemos muchos condicionales uno dentro de otro, el código se desplaza hacia la derecha. Esto se conoce como la pirámide de la muerte o código espagueti. Es pésimo porque se vuelve ilegible."
• Cláusulas de Guarda: "La solución profesional es evaluar los errores o exclusiones primero para limpiar el camino principal. Así el código se mantiene plano y lineal."
• Nueva Temática: "Para cerrar la teoría, usaremos la temática de un Gimnasio Inteligente. Verificaremos las condiciones para que un usuario pueda ingresar a la sala de máquinas (membresía activa y calzado adecuado)."
"""

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
        print("• Acceso concedido. ¡Disfruta tu entrenamiento!")
    else:
        print("• Error: Por seguridad, no puedes ingresar sin tenis deportivos.")
else:
    print("• Error: Tu membresía expiró o no está registrada en el sistema.")


# ------------------------------------------------------------------------------
# * 8.2 La Solución: Cláusulas de Guarda (Código Profesional y Plano)
# ------------------------------------------------------------------------------
# ? Mismo problema, pero descartando los errores de forma inmediata al inicio
print("\n--- Enfoque Profesional (Cláusulas de Guarda) ---")

# * 1. Descartamos el primer error de forma directa
if not tiene_membresia:
    print("• Error: Tu membresía expiró o no está registrada en el sistema.")
    # ! Nota para el profesor: En una función real, aquí usaríamos un 'return' para cortar la ejecución.

# * 2. Descartamos el segundo error de forma directa
if not trae_calzado_deportivo:
    print("• Error: Por seguridad, no puedes ingresar sin tenis deportivos.")

# * 3. El "Camino Feliz" (Éxito) queda completamente libre de anidaciones
if tiene_membresia and trae_calzado_deportivo:
    print("• Acceso concedido. ¡Disfruta tu entrenamiento!")




