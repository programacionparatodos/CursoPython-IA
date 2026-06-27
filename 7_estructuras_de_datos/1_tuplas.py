# ==============================================================================
# # 7_estructuras_de_datos -> 1_tuplas.py
# ==============================================================================

# ==============================================================================
# * INTRODUCCIÓN A LAS TUPLAS (TUPLES)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 1.1 ¿Qué es una Tupla y cuál es su sintaxis básica?
# ------------------------------------------------------------------------------

# * Representación de las dimensiones fijas de una pantalla de interfaz gráfica (Ancho, Alto)
resolucion_pantalla = (1920, 1080)
print("--- Inicialización de una Tupla ---")
print(f"Resolución de pantalla configurada: {resolucion_pantalla}")
print(f"Tipo de estructura: {type(resolucion_pantalla)}")

# ------------------------------------------------------------------------------
# * 1.2 Importancia y casos de uso en el mundo real (¿Para qué sirven?)
# ------------------------------------------------------------------------------

# * Datos de conexión de red fijos para los servidores centrales de una aplicación
conexion_servidor = ("192.168.1.50", 5432)
print("\n--- Casos de Uso Real (Datos Fijos) ---")
print(f"IP del servidor: {conexion_servidor[0]}")
print(f"Puerto de escucha: {conexion_servidor[1]}")

# * Demostración de seguridad de datos (Descomentar para mostrar el error de bloqueo)
# conexion_servidor[0] = "10.0.0.1" 
# ! ERROR: Generará un 'TypeError'. Las tuplas protegen los datos contra accidentes.

# ------------------------------------------------------------------------------
# * 1.3 Los únicos métodos disponibles para las Tuplas
# ------------------------------------------------------------------------------

# * Siglas de las ciudades donde opera un sistema logístico
estados_cobertura = ("OR", "LP", "CB", "OR", "SC")

# * Uso del método .count() para saber la frecuencia de un dato
repeticiones = estados_cobertura.count("OR")

# * Uso del método .index() para localizar la posición del primer encuentro
posicion = estados_cobertura.index("CB")

print("\n--- Métodos de Lectura Disponibles ---")
print(f"Veces que aparece 'OR' en la tupla: {repeticiones}")
print(f"La ciudad 'CB' se encuentra en el índice: {posicion}")

# ! NOTA: En programación se empieza a contar desde la posición 0 (0 es 'OR', 1 es 'LP'...).


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: La trampa del elemento único sin coma
# ? Si creas una tupla con un solo elemento y olvidas colocar una coma al final, Python 
# ? pensará que son paréntesis matemáticos comunes y creará una variable de texto (str).
falsa_tupla = ("Config_Usuario")     # Tipo: str (Incorrecto)
tupla_verdadera = ("Config_Usuario",) # Tipo: tuple (Correcto debido a la coma)

print("\n--- Refuerzo: Casos Especiales ---")
print(f"Tipo detectado sin coma final: {type(falsa_tupla)}")
print(f"Tipo detectado con coma final: {type(tupla_verdadera)}")

# * Ejemplo B: Desempaquetado rápido de datos
# ? Python permite asignar los elementos internos de una tupla directamente a variables 
# ? individuales en una sola línea de código, distribuyendo los valores en orden.
config_color_rgb = (255, 128, 0)
rojo, verde, azul = config_color_rgb 

print(f"Componente Rojo extraído: {rojo}")
print(f"Componente Verde extraído: {verde}")
print(f"Componente Azul extraído: {azul}")