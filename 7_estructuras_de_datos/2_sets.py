# ==============================================================================
# # 7_estructuras_de_datos -> 2_sets.py
# ==============================================================================

# ==============================================================================
# * INTRODUCCIÓN A LOS CONJUNTOS (SETS)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 ¿Qué es un Set y cuál es su sintaxis básica?
# ------------------------------------------------------------------------------

# * Registro de números de ticket de clientes (Observa el elemento duplicado 505)
tickets_atencion = {501, 502, 505, 503, 505, 504}
print("--- Inicialización de un Set ---")
print(f"Contenido del conjunto en pantalla: {tickets_atencion}")
print(f"Tipo de estructura: {type(tickets_atencion)}")
# ! NOTA: Mira la pantalla; el número 505 apareció una sola vez y el orden cambió.

# ------------------------------------------------------------------------------
# * 2.2 Importancia y casos de uso en el mundo real (¿Para qué sirven?)
# ------------------------------------------------------------------------------

# * Colección heterogénea (Sí permite datos mezclados al igual que las tuplas)
datos_unicos = {"ID_88", 12.5, True, 2026}
print("\n--- Flexibilidad y Uso Real ---")
print(f"Set con tipos de datos mezclados: {datos_unicos}")


# ------------------------------------------------------------------------------
# * 2.3 Métodos fundamentales para manipular Conjuntos
# ------------------------------------------------------------------------------

# * Creamos un conjunto inicial de productos vistos por un usuario
productos_interes = {"Laptop", "Celular"}

# * .add(elemento) -> Agrega un elemento nuevo al conjunto
productos_interes.add("Audífonos")
productos_interes.add("Laptop") # Intentamos meter un duplicado

# * .remove(elemento) -> Elimina un elemento específico. Lanza error si no existe.
productos_interes.remove("Celular")

# * .discard(elemento) -> Elimina un elemento específico, pero NO lanza error si no existe.
productos_interes.discard("Teclado") # 'Teclado' no está, pero el programa no se rompe

print("\n--- Métodos de Modificación ---")
print(f"Conjunto final tras aplicar métodos: {productos_interes}")


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: La trampa del Set vacío (Creación incorrecta)
# ? Si intentas crear un conjunto vacío usando solo llaves `{}`, Python asumirá de 
# ? forma predeterminada que estás creando un Diccionario vacío. Para crear un set 
# ? totalmente vacío, debes usar obligatoriamente la función constructora `set()`.
falso_set_vacio = {}
verdadero_set_vacio = set()

print("\n--- Refuerzo: Trampas y Trucos ---")
print(f"Estructura creada con '{{}}': {type(falso_set_vacio)}")
print(f"Estructura creada con 'set()': {type(verdadero_set_vacio)}")

# * Ejemplo B: Operaciones matemáticas avanzadas con Sets (Intersección)
# ? Los sets permiten saber instantáneamente qué elementos tienen en común dos colecciones 
# ? utilizando el operador ampersand (&). Esto se usa en aplicaciones reales como Netflix 
# ? para recomendarte películas que le gustaron a dos amigos al mismo tiempo.
gustos_juan = {"Acción", "Terror", "Sci-Fi"}
gustos_maria = {"Comedia", "Drama", "Terror"}

gustos_en_comun = gustos_juan & gustos_maria # Busca el elemento repetido en ambos

print(f"Géneros de películas que les gustan a ambos: {gustos_en_comun}")


# * Ejemplo C: Fusión total de datos únicos (Unión)
# ? El operador de barra vertical (|) une dos conjuntos eliminando cualquier elemento 
# ? que esté repetido entre ambos. Es sumamente útil para consolidar bases de datos 
# ? diferentes sin duplicar registros de clientes.
contactos_tienda_oruro = {"Carlos", "Ana", "Pedro"}
contactos_tienda_lapaz = {"Maria", "Ana", "Juan"}

# ? Unimos ambas listas de contactos eliminando los duplicados automáticamente
todos_los_contactos = contactos_tienda_oruro | contactos_tienda_lapaz

print(f"Lista consolidada de contactos únicos: {todos_los_contactos}")
# ! NOTA: Observa cómo 'Ana' aparece una sola vez en el resultado final.


# * Ejemplo D: Filtrado de exclusión de datos (Diferencia)
# ? El operador de resta (-) quita del primer conjunto todos los elementos que también 
# ? existan en el segundo conjunto. En el desarrollo web se usa para saber con exactitud 
# ? qué usuarios se registraron a un evento pero que todavía no han pagado su entrada.
usuarios_registrados = {"Luis", "Marcos", "Elena", "Sofia"}
usuarios_que_pagaron = {"Marcos", "Sofia"}

# ? Restamos los que pagaron para obtener únicamente a los deudores pendientes
usuarios_morosos = usuarios_registrados - usuarios_que_pagaron

print(f"Usuarios que se registraron pero no han pagado: {usuarios_morosos}")


# * Ejemplo E: Encontrar elementos totalmente exclusivos (Diferencia Simétrica)
# ? El operador de acento circunflejo (^) compara dos conjuntos y devuelve un nuevo 
# ? conjunto con los elementos que están en uno o en otro, pero NO en ambos a la vez. 
# ? Sirve para detectar productos que solo se venden en una sucursal específica.
inventario_sucursal_A = {"Teclado", "Mouse", "Monitor"}
inventario_sucursal_B = {"Teclado", "Mouse", "Impresora"}

# ? Extrae lo que es exclusivo de cada tienda, descartando lo que comparten en común
productos_exclusivos = inventario_sucursal_A ^ inventario_sucursal_B

print(f"Productos que no se comparten entre sucursales: {productos_exclusivos}")