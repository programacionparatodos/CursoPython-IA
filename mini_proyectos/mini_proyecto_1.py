# ==============================================================================
# mini_proyectos -> mini_proyecto_1.py
# ==============================================================================
# ? Objetivo: Integrar variables, constantes, entradas, salidas y casting de tipos.
# ? Dinámica: Crear una historia multicultural interactiva simulando la participación de la clase.

# ==============================================================================
# * MINI PROYECTO 1: CREANDO UNA HISTORIA LOCA INTERCULTURAL
# ==============================================================================

# ==========================================
# * 1. CONFIGURACIÓN INICIAL (Constantes)
# ==========================================
# ? Recordatorio: Al estar en MAYÚSCULAS respetamos el contrato social de no modificarlas.
IDIOMA_CURSO = "Español"
POBLACION_GUAYAQUIL = 3_007_696  # Uso correcto del guion bajo como separador visual.


# ==========================================
# * 2. ENTRADA DE DATOS (Interactiva)
# ==========================================
print("=== ¡BIENVENIDOS AL CURSO INTERNACIONAL DE PYTHON + IA! ===")
print("Vamos a conocernos creando una historia divertida en el curso.\n")

# ? La función input() siempre devuelve una cadena de texto (str).
nombre_alumno = input("Estudiante 1: ¿Cuál es tu nombre?: ")
pais_origen = input("Estudiante 2: ¿De qué país te conectas?: ")
comida_tipica = input("Estudiante 3: Dinos una comida típica de tu país: ")

# ! ALERTA: Conversión explícita obligatoria a Entero (int)
cantidad_comida = int(input("Estudiante 4: ¿Cuántas porciones te comerías ahora mismo?: "))

# ! ALERTA: Conversión explícita obligatoria a Flotante (float)
precio_dolares = float(input("Estudiante 5: ¿Cuánto cuesta una porción en dólares?: "))    

# ! ALERTA: Evaluación lógica indirecta para obtener un Booleano (bool)
respuesta_viaje = input("Estudiante 6: ¿Tienes miedo de viajar en avión? (si/no): ")
miedo_a_viajar_en_avion = (respuesta_viaje == "si")


# ==========================================
# * 3. PROCESAMIENTO DE DATOS
# ==========================================
# ? Coerción implícita: int * float resulta en un tipo 'float'.
costo_banquete = cantidad_comida * precio_dolares  


# ==========================================
# * 4. SALIDA DE DATOS (La Gran Historia)
# ==========================================
print("\nConectando con los servidores del mundo", end="... ")
print("¡HISTORIA LISTA!\n")

# * Usamos f-strings para estructurar la salida de forma limpia y moderna.
print(f"Hoy le damos la bienvenida oficial a {nombre_alumno}, quien viene desde {pais_origen}.")
print(f"Para celebrar su llegada, nos va a invitar {comida_tipica} a todos.")
print(f"Como hay mucha hambre, calcula que el grupo necesita {cantidad_comida} porciones.")
print(f"Cada una cuesta ${precio_dolares}, así que la cuenta total será de ${costo_banquete:.2f}.")
print(f"¿Tiene nuestro compañero pánico a volar para venir al evento?: {miedo_a_viajar_en_avion}\n")


# ==========================================
# * 5. REPORTE DEL SISTEMA (Verificación de Constantes)
# ==========================================
# ? Mostramos las constantes para verificar que sus valores permanecieron inalterados.
print("==========================================")
print("             REPORTE FINAL                ")
print("==========================================")
print(f"• Idioma oficial del curso verificado: {IDIOMA_CURSO}")
print(f"• Población base registrada en base de datos: {POBLACION_GUAYAQUIL:_}") 
# ? Nota técnica: Usar :_ dentro de las llaves vuelve a ponerle los guiones bajos al imprimirlo en consola.
print("==========================================")

# TODO: Recordar que luego de este mini proyecto avanzaremos operadores aritméticos y manejo de cadenas