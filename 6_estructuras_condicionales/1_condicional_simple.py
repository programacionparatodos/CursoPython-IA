# ==============================================================================
# # 6_condicionales -> 1_condicional_simple.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 3: LA CONDICIONAL SIMPLE
# ==============================================================================

# ------------------------------------------------------------------------------
# * 3.1 Filtro de umbral único (Uso de una vía)
# ------------------------------------------------------------------------------
# ? Sensor del tanque de gasolina del automóvil (en porcentaje)
nivel_combustible = 12

print("Sistema de diagnóstico del vehículo iniciado...")

# * Si el combustible baja del 15%, se despliega una advertencia en el tablero
if nivel_combustible < 15:
    print("[ALERTA] Nivel de combustible crítico detectado.")
    print("-> Sugiriendo ruta hacia la estación de servicio más cercana.")

print("Monitoreo de sensores en segundo plano activo.")

# ! NOTA: Si el nivel fuera 50, el bloque interno del 'if' se omitiría por completo.
# TODO: Error común de olvidar los dos puntos (:) al final del 'if'.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Evitando la ejecución accidental fuera del bloque 'if'
# ? Recuerda que la sangría define qué está dentro del condicional. Si quitas los 4 espacios,
# ? la línea se ejecutará siempre, sin importar si la condición es verdadera o falsa.
temperatura_motor = 85  # Rango normal en grados

print("Verificando estado del motor del automóvil...")
if temperatura_motor > 100:
    print("[ALERTA CRÍTICA] ¡Motor sobrecalentado! Detenga el vehículo.") # No se ejecuta
print("-> Ventilador del radiador encendido al máximo.") # ! ERROR: Se ejecuta siempre por mala sangría

# * Ejemplo B: Evaluando estados booleanos directamente (Sin usar == True)
# ? Escribir 'if variable == True:' funciona, pero es redundante. En Python profesional
# ? pasamos la variable booleana directamente, ya que el 'if' evalúa su valor interno.
freno_mano_puesto = True

# * Enfoque limpio y directo para el sistema del coche
if freno_mano_puesto:
    print("[AVISO] El freno de mano sigue activo. Desactívelo antes de avanzar.")

# * Ejemplo C: El peligro de modificar el tipo de datos antes del 'if'
# ? Si el sensor del coche devuelve un texto en lugar de un número, el condicional fallará catastróficamente.
velocidad_sensor = "120"  # Viene como texto desde el software del velocímetro

# if velocidad_sensor > 100: # ❌ Esto lanzará un TypeError: no se puede comparar str con int
#     print("Reduciendo velocidad de crucero automáticamente.")

# * Solución Profesional: Casteo preventivo antes de evaluar la condición
if int(velocidad_sensor) > 100:
    print("[ASISTENCIA] Velocidad alta. Activando alerta de mantenimiento de carril.") # Muestra este mensaje


