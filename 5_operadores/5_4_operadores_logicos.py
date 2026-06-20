# ==============================================================================
# # 5_operadores -> 5_4_operadores_logicos.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 2: OPERADORES LÓGICOS
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 El Operador de Cumplimiento Estricto (and)
# ------------------------------------------------------------------------------
# ? Control de embarque: El pasajero necesita pasaporte vigente Y boleto físico o digital
tiene_pasaporte = True
tiene_boleto = True

# * Ambas condiciones deben ser True para permitirle subir al avión
permitir_abordaje = tiene_pasaporte and tiene_boleto
print("¿El pasajero puede abordar el avión?:", permitir_abordaje)

# ------------------------------------------------------------------------------
# * 2.2 El Operador de Flexibilidad (or) y de Inversión (not)
# ------------------------------------------------------------------------------
# ? Beneficios de equipaje: El cliente viaja gratis con maleta si es VIP O si pagó equipaje extra
es_miembro_vip = False
pago_maleta_extra = True

# * Con que una de las dos opciones sea True, el equipaje está autorizado
equipaje_autorizado = es_miembro_vip or pago_maleta_extra
print("¿El equipaje está aprobado para bodega?:", equipaje_autorizado)

# ? Lista de exclusión aérea: Verificamos si el pasajero NO tiene restricciones de seguridad
pasajero_vetado = False

# * El operador 'not' invierte el valor lógico actual para validar un estado limpio
print("¿El pasajero está libre de alertas de seguridad?:", not pasajero_vetado)


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: La trampa de evaluar textos vacíos en condiciones lógicas
# ? En Python, un texto vacío "" equivale lógicamente a False, y un texto con contenido equivale a True.
# ? Validamos si el pasajero olvidó escribir su nombre en el formulario de la aerolínea.
nombre_pasajero = ""
print("¿El campo de nombre está vacío?:", not nombre_pasajero) # Muestra: True

# * Ejemplo B: Cortocircuito lógico con el operador 'and'
# ? Python lee de izquierda a derecha. Si en un 'and' la primera condición es False, 
# ? Python no pierde tiempo leyendo la segunda, la ignora por completo (Short-circuit evaluation).
vuelo_confirmado = False
sistema_pago_activo = True  # Imagina que este servidor está caído y tarda en responder

# * Como 'vuelo_confirmado' es False, el sistema ni siquiera consulta si el pago está activo
print("¿Se puede emitir el pase de abordar?:", vuelo_confirmado and sistema_pago_activo) # Muestra: False

# * Ejemplo C: Prioridad de operadores (and tiene más peso que or)
# ? Sin paréntesis, Python evalúa primero los 'and' y luego los 'or'. ¡Usa paréntesis para evitar desastres!
# ? Regla: Viaja gratis si es diplomático OR si tiene boleto comercial AND maleta pesada.
es_diplomatico = True
tiene_boleto = False
maleta_pesada = False

# * Lógica sin paréntesis (Peligro: da True porque evalúa: es_diplomatico or (tiene_boleto and maleta_pesada))
resultado_incorrecto = es_diplomatico or tiene_boleto and maleta_pesada
print("Resultado sin control manual:", resultado_incorrecto) # Muestra: True

# * Lógica correcta usando paréntesis para agrupar las condiciones del pasajero común
resultado_correcto = (es_diplomatico or tiene_boleto) and maleta_pesada
print("Resultado ordenado con paréntesis:", resultado_correcto) # Muestra: False