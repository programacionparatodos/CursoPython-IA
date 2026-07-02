# ==============================================================================
# # 7_estructuras_de_datos -> 5_anidamiento.py
# ==============================================================================

# ==============================================================================
# * ANIDAMIENTO DE ESTRUCTURAS (COMBINANDO LISTAS Y DICCIONARIOS)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 5.1 ¿Qué es el anidamiento y por qué es la estructura definitiva?
# ------------------------------------------------------------------------------

# * Creamos diccionarios individuales que representan personajes de un juego
enemigo_1 = {"nombre": "Duende", "vida": 50, "puntos": 10}
enemigo_2 = {"nombre": "Ogro", "vida": 150, "puntos": 50}

# * Creamos la Lista "Base de Datos" y anidamos los diccionarios adentro
base_datos_juego = [enemigo_1, enemigo_2]

print("--- Inicialización de Estructuras Anidadas ---")
print(f"Base de datos del juego completa:\n{base_datos_juego}")

# ------------------------------------------------------------------------------
# * 5.2 Acceso bidireccional: ¿Cómo extraer un dato específico?
# ------------------------------------------------------------------------------

print("\n--- Acceso Complejo a Datos Anidados ---")

# * Extraemos el nombre del primer personaje (Lista posición 0 -> Diccionario clave 'nombre')
nombre_primer_enemigo = base_datos_juego[0]["nombre"]
print(f"El primer enemigo en la lista es: {nombre_primer_enemigo}")

# * Extraemos la vida del segundo personaje (Lista posición 1 -> Diccionario clave 'vida')
vida_segundo_enemigo = base_datos_juego[1]["vida"]
print(f"La vida del segundo enemigo ({base_datos_juego[1]['nombre']}) es de: {vida_segundo_enemigo} HP")

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Agregar un diccionario nuevo a la lista dinámicamente
# ? Podemos usar el método '.append()' que aprendimos en las listas para inyectar 
# ? un nuevo diccionario completo al final de nuestra colección en tiempo de ejecución.
# servidores_activos = [
#     {"pais": "Bolivia", "ping": 15},
#     {"pais": "Brasil", "ping": 45}
# ]
# print(f"\nLista de servidores original: {servidores_activos}")

# * Creamos un nuevo servidor y lo enganchamos al final de la lista
# nuevo_servidor = {"pais": "Argentina", "ping": 30}
# servidores_activos.append(nuevo_servidor)

# print(f"Lista de servidores actualizada: {servidores_activos}")


# * Ejemplo B: Modificar una característica interna de un elemento anidado
# ? Si el estado de un objeto cambia, apuntamos primero a su posición en la lista 
# ? y luego a la clave del diccionario para alterar su valor directamente en la RAM.
# inventario_tienda = [
#     {"item": "Laptop", "stock": 5},
#     {"item": "Mouse", "stock": 20}
# ]

# * Simulamos que se vendió una Laptop: disminuimos su stock (Lista índice 0 -> Clave 'stock')
# inventario_tienda[0]["stock"] = inventario_tienda[0]["stock"] - 1

# print(f"Inventario actualizado tras una venta: {inventario_tienda}")


# * Ejemplo C: El caso inverso (Una Lista dentro de un Diccionario)
# ? El anidamiento también funciona al revés. Un diccionario puede tener una clave 
# ? cuyo valor sea una lista completa de elementos sueltos.
# perfil_estudiante = {
#     "nombre": "Alejandro",
#     "materias_aprobadas": ["Programación I", "Álgebra", "Física I"]
# }

# * Accedemos a la segunda materia aprobada (Diccionario clave -> Lista índice 1)
# segunda_materia = perfil_estudiante["materias_aprobadas"][1]

# print(f"Estudiante: {perfil_estudiante['nombre']}")
# print(f"La segunda materia que aprobó fue: {segunda_materia}")


# * TODOS LOS TIPOS DE ANIDAMIENTO

# * Una LISTA que contiene Tuplas, Sets y Diccionarios
# ? Como la lista es un contenedor lineal libre, cada uno de sus vagones puede 
# ? albergar una estructura totalmente diferente de forma consecutiva.
# contenedor_lista = [
#     ("IP_Servidor", 8080),            # Vagón 0: Una Tupla (datos fijos)
#     {"Invitado_1", "Invitado_2"},    # Vagón 1: Un Set (nombres únicos)
#     {"id": 101, "rol": "Admin"}      # Vagón 2: Un Diccionario (clave-valor)
# ]

# print("\n--- Refuerzo A: La Lista como contenedor global ---")
# print(f"Lista mezclada: {contenedor_lista}")
# print(f"-> Extrayendo la tupla del índice 0: {contenedor_lista[0]}")


# * Una TUPLA que contiene Listas, Sets y Diccionarios
# ? ¡Ojo aquí! La tupla sigue siendo inmutable (no puedes quitarle el vagón 0 ni el 1), 
# ? pero si metes una lista dentro de una tupla, ¡los elementos internos de esa lista 
# ? sí se pueden modificar! La tupla solo congela las identidades de sus contenedores.
# contenedor_tupla = (
#     ["Modo_Oscuro", "Español"],      # Posición 0: Una Lista (modificable)
#     {10, 20, 30},                    # Posición 1: Un Set (valores únicos)
#     {"web": "google.com"}            # Posición 2: Un Diccionario
# )

# * Demostración de modificación interna permitida dentro de una tupla
# contenedor_tupla[0].append("Fuentes_Grandes") # Modificamos la lista interna

# print("\n--- Refuerzo B: La Tupla como contenedor global ---")
# print(f"Tupla mezclada: {contenedor_tupla}")
# print(f"-> Lista interna modificada dentro de la tupla: {contenedor_tupla[0]}")


# * Un DICCIONARIO que contiene Listas, Tuplas y Sets
# ? Es la estructura más usada en la industria. Te permite etiquetar cada tipo 
# ? de colección con una clave con nombre para saber exactamente qué estás leyendo.
# contenedor_diccionario = {
#     "lista_tareas": ["Programar", "Estudiar"],
#     "tupla_coordenadas": (-16.5000, -68.1500),
#     "set_codigos_unicos": {"PROMO1", "PROMO2"}
# }

# print("\n--- Refuerzo C: El Diccionario como contenedor global ---")
# print(f"Diccionario mezclado: {contenedor_diccionario}")
# print(f"-> Extrayendo el set mediante su clave: {contenedor_diccionario['set_codigos_unicos']}")


# * Un SET (Conjunto) que contiene... ¡CUIDADO! Solo Tuplas
# ? Aquí hay una regla de oro estricta en Python: Como los Sets necesitan calcular 
# ? de forma matemática que nada se repita, SOLO permiten almacenar elementos que sean 
# ? INMUTABLES. Por lo tanto, un Set puede contener Tuplas, pero si intentas meterle 
# ? una Lista o un Diccionario, el programa lanzará un error crítico ('TypeError: unhashable type').
# contenedor_set = {
#     (1, 2), 
#     (3, 4), 
#     (1, 2) # Duplicado que el set borrará automáticamente
# }

# print("\n--- Refuerzo D: El Set como contenedor limitado ---")
# print(f"Set de tuplas (duplicados eliminados): {contenedor_set}")
# ! ADVERTENCIA: Nunca intentes meter una lista o diccionario directo en un set, por ejemplo:
# ! mi_set = {[1, 2]}  o  mi_set = {{"clave": "valor"}}
# ! Esto romperá el programa porque las listas y diccionarios pueden cambiar de tamaño.
