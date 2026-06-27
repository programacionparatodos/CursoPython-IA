# ==============================================================================
# # 7_estructuras_de_datos -> 4_diccionarios.py
# ==============================================================================

# ==============================================================================
# * INTRODUCCIÓN A LOS DICCIONARIOS (DICTIONARIES)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 4.1 ¿Qué es un Diccionario y cuál es su sintaxis básica?
# ------------------------------------------------------------------------------

# * Creamos nuestro primer diccionario vacío (un contenedor estructurado)
datos_usuario = {}

# * Creamos un diccionario con datos precargados: las propiedades de una PC
perfil_computadora = {
    "marca": "Asus",
    "ram_gb": 16,
    "es_laptop": True
}

print("--- Inicialización de Diccionarios ---")
print(f"Estado inicial del diccionario vacío: {datos_usuario}")
print(f"Perfil de la computadora: {perfil_computadora}")
print(f"Tipo estructura: {type(perfil_computadora)}")

# ------------------------------------------------------------------------------
# * 4.2 Acceso y modificación de datos mediante Claves
# ------------------------------------------------------------------------------

print("\n--- Lectura y Modificación ---")

# * Accedemos a leer un dato específico usando su clave
memoria_actual = perfil_computadora["ram_gb"]
print(f"La memoria RAM actual de la PC es de: {memoria_actual} GB")

# * Modificamos o actualizamos un valor existente en tiempo real (Casteo o actualización)
perfil_computadora["ram_gb"] = 32
print(f"Perfil tras repotenciar la memoria RAM: {perfil_computadora}")

# TODO: Error común de novato -> Escribir una clave que no existe (ej. perfil_computadora["precio"]).
# TODO: Provocará un error de tipo 'KeyError' que detendrá el programa por completo.

# ------------------------------------------------------------------------------
# * 4.3 Métodos Esenciales para manipular Diccionarios
# ------------------------------------------------------------------------------

print("\n--- Métodos del Diccionario ---")

# * Obtenemos todas las claves del perfil
lista_de_claves = perfil_computadora.keys()
print(f"Claves disponibles en la estructura: {lista_de_claves}")

# * Obtenemos todos los valores del perfil
lista_de_valores = perfil_computadora.values()
print(f"Valores almacenados en la estructura: {lista_de_valores}")

# * Uso seguro de .get() para evitar que el sistema colapse ante datos inexistentes
busqueda_segura = perfil_computadora.get("tarjeta_video", "No especificada")
print(f"Resultado de la búsqueda segura de tarjeta gráfica: {busqueda_segura}")


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Agregar una clave completamente nueva al diccionario
# ? A diferencia de las listas que necesitan '.append()', para agregar una clave nueva 
# ? a un diccionario simplemente la escribes entre corchetes y le asignas su valor.
estado_sistema = {"usuario": "Admin", "estado": "Activo"}
print(f"\nEstado inicial: {estado_sistema}")

# * Agregamos un campo que no existía antes en la estructura
estado_sistema["id_sesion"] = 99452
print(f"Estado actualizado con campo nuevo: {estado_sistema}")


# * Ejemplo B: Eliminar una clave y su valor del diccionario (Palabra clave del)
# ? Si un dato ya no es necesario o el usuario decide dar de baja un parámetro, 
# ? podemos borrar la clave por completo usando la instrucción nativa 'del'.
config_juego = {"resolucion": "1080p", "musica": True, "sombras": "Altas"}
print(f"Configuración del juego (Antes): {config_juego}")

# * Eliminamos el parámetro de las sombras de los gráficos
del config_juego["sombras"]
print(f"Configuración del juego (Después): {config_juego}")


# * Ejemplo C: El método .update() para modificar múltiples campos a la vez
# ? Si necesitas cambiar muchos datos de un solo golpe en lugar de escribir 
# ? línea por línea, puedes pasarle un mini diccionario con los cambios al método .update().
perfil_servidor = {"host": "localhost", "puerto": 80, "online": False}
print(f"Servidor original: {perfil_servidor}")

# * Aplicamos una actualización masiva de parámetros
perfil_servidor.update({"puerto": 443, "online": True})
print(f"Servidor actualizado con .update(): {perfil_servidor}")
