# ==============================================================================
# # 6_condicionales -> 4_operador_ternario.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 6: EL OPERADOR TERNARIO
# ==============================================================================

# ------------------------------------------------------------------------------
# * 6.1 Simplificación de Estructuras Dobles en una Línea
# ------------------------------------------------------------------------------
# ? Caso 1: Verificar el estado visual de una habitación en el sistema del hotel
habitacion_limpia = True

# * Forma tradicional en 4 líneas (Comentada para comparar)
# if habitacion_limpia:
#     estado = "DISPONIBLE"
# else:
#     estado = "EN MANTENIMIENTO"

# * Enfoque con Operador Ternario: Compacto y directo
estado_habitacion = "DISPONIBLE" if habitacion_limpia else "EN MANTENIMIENTO"
print("Recepción:", estado_habitacion)

# ------------------------------------------------------------------------------
# * 6.2 Uso del Ternario directamente dentro de un print()
# ------------------------------------------------------------------------------
# ? Caso 2: Control de acceso rápido a la piscina en el torniquete de entrada
tiene_brazalete_vip = False

# * Evaluamos la condición directamente al momento de imprimir el mensaje
# ! ALERTA: No abusar de esto si la lógica se vuelve muy larga o difícil de leer
print("Acceso Piscina:", "PERMITIDO" if tiene_brazalete_vip else "RESTRINGIDO")

# TODO: el operador ternario en Python SIEMPRE exige la parte 'else'.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Formatear la salida de datos numéricos para el usuario final
# ? A veces queremos mostrar un texto amigable en lugar de un número crudo en la factura.
# ? Caso: Si el costo de estacionamiento es 0, mostramos "GRATIS" en lugar de "$0".
costo_estacionamiento = 0

# * El ternario evalúa el número y decide si asigna un texto o la cifra formateada
mensaje_cobro = "GRATIS" if costo_estacionamiento == 0 else f"${costo_estacionamiento}"
print(f"Tarifa de cochera del hotel: {mensaje_cobro}")

# * Ejemplo B: El peligro de la anidación de operadores ternarios (Código ilegible)
# ? ¡Cuidado! Es posible meter un operador ternario dentro de otro ternario. 
# ? Aunque Python lo permite, es una PÉSIMA práctica porque rompe la legibilidad.
# ? Caso: Asignar piso según tipo de cliente: VIP -> Piso 5, Frecuente -> Piso 3, Estándar -> Piso 1.
es_vip = False
es_frecuente = True

# * ❌ EVITAR ESTO EN LA VIDA REAL: Código difícil de leer de un solo vistazo
piso_asignado = 5 if es_vip else (3 if es_frecuente else 1)
print("Habitación asignada en el nivel:", piso_asignado)

# TODO: Reescribir el Ejemplo B usando una estructura 'if-elif-else' tradicional para notar la diferencia con claridad.

