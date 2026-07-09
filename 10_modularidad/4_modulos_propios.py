# ==============================================================================
# # 10_modularidad -> 4_modulos_propios.py
# ==============================================================================

# ==============================================================================
# * MODULARIDAD II: IMPORTAR NUESTROS PROPIOS ARCHIVOS DE PYTHON
# ==============================================================================

# * Importamos nuestro archivo de herramientas aritméticas y le ponemos un alias
import mis_herramientas as math_casero

print("--- 4.1 Consumiendo nuestra función clonada tam() ---")
# * Tipo de dato: Lista (list) con canciones de un álbum
album_canciones = ["Song A", "Song B", "Song C", "Song D"]

# * Usamos nuestra propia función 'tam' en lugar del 'len' oficial de Python
cantidad_canciones = math_casero.tam(album_canciones)
print(f"🎵 El álbum musical tiene: {cantidad_canciones} canciones en total.")


# ------------------------------------------------------------------------------
# * 4.2 Invocación de Operaciones Avanzadas del Módulo
# ------------------------------------------------------------------------------

print("\n--- 4.2 Calculando Promedios con Datos Reales ---")
# * Tipo de dato: Lista (list) con las calificaciones floats de una película
calificaciones_usuarios = [8.5, 9.0, 7.2, 10.0, 6.8]

# * Invocamos la función matemática compleja de nuestro módulo propio
promedio_final = math_casero.calcular_promedio(calificaciones_usuarios)
print(f"🎬 La calificación promedio de la película es de: {promedio_final}/10")


# ------------------------------------------------------------------------------
# * 4.3 Invocación Directa con From / Import Propio
# ------------------------------------------------------------------------------

from mis_herramientas import tam

print("\n--- 4.3 Extracción Específica desde Módulo Propio ---")
# * Tipo de dato: Diccionario (dict) con los datos del perfil de una mascota
perfil_mascota = {"nombre": "Rocco", "especie": "Perro", "edad": 4, "vacunado": True}

# * Usamos 'tam' directamente para contar cuántas llaves/propiedades tiene el diccionario
total_propiedades = tam(perfil_mascota)
print(f"🐾 El perfil de la mascota tiene {total_propiedades} datos registrados.")


# ------------------------------------------------------------------------------
# * 4.4 El Misterio de la variable secreta `__name__`
# ------------------------------------------------------------------------------

print("\n--- 4.4 Inspección de Seguridad del archivo ---")
print(f"Nombre en memoria del módulo importado: {math_casero.__name__}")
print(f"Nombre en memoria de este archivo actual: {__name__}")

# ! ALERTA: Como el archivo 'mis_herramientas' se cargó con su nombre real en memoria 
# ! y NO como "__main__", su escudo bloqueó las líneas de prueba y la consola quedó limpia.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Creación de un Validador de Textos Vacíos (Uso de Strings y tam)
# ? Podemos crear una función aritmética rápida que verifique si un usuario dejó 
# ? una caja de texto vacía midiendo su longitud con nuestra función casera.
def es_texto_vacio(cadena_texto):
    if tam(cadena_texto) == 0:
        return True
    return False

print("\n--- Refuerzo A: Validando Strings con tam() ---")
entrada_usuario = "" # str vacía
if es_texto_vacio(entrada_usuario):
    print("❌ [ERROR] El nombre de usuario no puede estar en blanco.")


# * Ejemplo B: Filtro de Números Pares de una Colección (Uso de Listas)
# ? Las funciones matemáticas secundarias pueden procesar colecciones completas 
# ? aplicando el operador residuo (%) para limpiar y devolver nuevas listas filtradas.
def extraer_numeros_pares(lista_datos):
    pares = []
    for numero in lista_datos:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print("\n--- Refuerzo B: Filtrado Aritmético de Listas ---")
ID_usuarios = [101, 102, 103, 104, 105, 106]
IDs_pares = extraer_numeros_pares(ID_usuarios)
print(f"IDs de servidores pares detectados: {IDs_pares}")


# * Ejemplo C: Sumatoria de Precios de un Carrito de Compras (Uso de Diccionarios)
# ? Una función aritmética externa puede recibir un diccionario de productos y precios 
# ? para calcular de forma limpia el total de una transacción comercial.
def calcular_total_carrito(carrito_compras):
    total_pago = 0.0
    for producto in carrito_compras:
        total_pago += carrito_compras[producto]
    return total_pago

print("\n--- Refuerzo C: Operaciones Financieras con Diccionarios ---")
entradas_cine = {"Boleto VIP": 12.50, "Palomitas Gigantes": 8.00, "Refresco": 3.50}
total_cuenta = calcular_total_carrito(entradas_cine)
print(f"Monto total a facturar en caja: ${total_cuenta}")


# * Ejemplo D: Conteo de Elementos Únicos sin Repetir (Uso de Sets y Tuplas)
# ? Podemos combinar tuplas inmutables y conjuntos (sets) dentro de una función 
# ? para auditar cuántos datos reales y únicos ingresaron al sistema aritmético.
def contar_valores_unicos(tupla_datos):
    conjunto_limpio = set(tupla_datos)
    return tam(conjunto_limpio) # Contamos el tamaño del set con nuestra función

print("\n--- Refuerzo D: Auditoría de Datos Únicos ---")
votos_peliculas = ("Batman", "Avatar", "Batman", "Spiderman", "Avatar") # tuple
cantidad_unicos = contar_valores_unicos(votos_peliculas)
print(f"Total de películas diferentes que recibieron votos: {cantidad_unicos}")
