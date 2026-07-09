# ==============================================================================
# # 10_modularidad -> 2_funciones_basicas.py
# ==============================================================================

# ==============================================================================
# * FUNCIONES BÁSICAS: CREANDO NUESTRAS PROPIAS AUTOMATIZACIONES CON 'DEF'
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 Declaración y Estructura Básica de un Bloque Reutilizable
# ------------------------------------------------------------------------------

# * Creamos una función estática para simular el inicio de un concierto (Usa str e int)
def encender_escenario():
    banda = "Coldplay" # Tipo de dato: str
    asistentes = 55000 # Tipo de dato: int
    print(f"🎸 [STADIUM] Encendiendo luces LED... ¡La banda {banda} sale a escena!")
    print(f"🔊 [AUDIO] Micrófonos activos para {asistentes} fanáticos saltando.")

# ! NOTA: Si ejecutas este archivo ahora mismo, la pantalla se quedará en blanco. 
# ! El código dentro de 'def' está guardado en la memoria, pero NO se moverá solo.


# ------------------------------------------------------------------------------
# * 2.2 Invocación o Llamada (Despertar el código memorizado)
# ------------------------------------------------------------------------------

print("--- 2.2 Despertando el código del escenario ---")
# * Activamos la caja de código llamándola directamente
encender_escenario()

# ------------------------------------------------------------------------------
# * 2.3 Procesar Estructuras de Datos Complejas dentro de un 'def'
# ------------------------------------------------------------------------------

# * Esta función procesa una lista de canciones y un diccionario técnico
def reproducir_playlist():
    # * Tipo de dato: Lista (list) con canciones desordenadas
    lista_canciones = ["Yellow", "Viva la Vida", "The Scientist"] 
    
    # * Tipo de dato: Diccionario (dict) con el estado de la consola de audio
    consola_audio = {"volumen": 85.5, "bajos": "Potenciados", "ecualizado": True} # str, float, bool
    
    print(f"\n🎧 [DJ-BOOT] Configuración de audio actual -> Volumen: {consola_audio['volumen']}%")
    print("🎵 Iniciando la lista de reproducción oficial:")
    
    # * Recorremos la lista de forma automatizada dentro de la función
    for cancion in lista_canciones:
        print(f"   ▶️ Sonando ahora mismo: {cancion}")

print("\n--- 2.3 Ejecución de Lógica Interna con Listas y Diccionarios ---")
reproducir_playlist() # Ejecutamos la automatización completa

# ------------------------------------------------------------------------------
# * 2.4 El Orden de Lectura de Python (El peligro del código fantasma)
# ------------------------------------------------------------------------------

print("\n--- 2.4 Comprobando el flujo del Intérprete ---")

# ! ALERTA: Si quitas el comentario de la línea de abajo, el programa se romperá 
# ! con un error 'NameError' porque Python todavía no sabe qué es 'apagar_luces'.
# apagar_luces() 

def apagar_luces():
    print("💤 [STADIUM] Concierto finalizado. Vaciando estadio y apagando generadores.")

apagar_luces() # * Correcto: Se invoca SOLO después de haber sido declarada arriba

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: El secreto del Ámbito Local (Variables que mueren dentro de la caja)
# ? Si creas una variable dentro de un 'def', esa variable pertenece únicamente a esa 
# ? función. No intentes llamarla desde el flujo general porque no existirá afuera.
def zona_vips():
    precio_pase_vip = 250.00 # Tipo de dato: float (Variable local)
    print(f"Acceso VIP habilitado. Costo interno: ${precio_pase_vip}")

print("\n--- Refuerzo A: Demostración de Ámbito ---")
zona_vips()
# print(precio_pase_vip) # ! Si activas esto, dará ERROR: 'precio_pase_vip' no está definido afuera.


# * Ejemplo B: Procesando Datos Inmutables del Concierto (Uso de Tuplas)
# ? Las tuplas guardan configuraciones fijas que la función lee pero no puede modificar, 
# ? garantizando la seguridad de datos críticos como ubicaciones o coordenadas del show.
def proyectar_pantallas_gigantes():
    # * Tipo de dato: Tupla (tuple) con las dimensiones fijas de la pantalla principal
    resolucion_pantalla = (1920, 1080) # int (Inmutable)
    print(f"🖥️ [VIDEO] Transmitiendo señal en vivo hacia las pantallas gigantes.")
    print(f"🖥️ [VIDEO] Ajustando proyectores a la resolución estricta de: {resolucion_pantalla}p.")

print("\n--- Refuerzo B: Lectura de Datos Inmutables con Tuplas ---")
proyectar_pantallas_gigantes()


# * Ejemplo C: Control de Acceso Eficiente sin Duplicados (Uso de Sets / Conjuntos)
# ? Los sets son ideales dentro de las funciones cuando necesitamos verificar listas 
# ? rápidas sin preocuparnos por elementos repetidos, como los códigos de entradas válidas.
def verificar_puertas_ingreso():
    # * Tipo de dato: Set (set) de IDs de boletos que ya cruzaron los torniquetes
    codigos_escaneados = {"TK-88", "TK-91", "TK-88", "TK-42"} # Notarás que 'TK-88' está duplicado
    print(f"🎟️ [TICKET-BOT] Procesando base de datos de control de acceso.")
    print(f"🎟️ [TICKET-BOT] Total de boletos únicos validados hasta ahora: {len(codigos_escaneados)}")
    print(f"🎟️ [TICKET-BOT] Listado de pases activos en el sistema: {codigos_escaneados}") # Elimina el duplicado solo

print("\n--- Refuerzo C: Filtrado Automático con Sets ---")
verificar_puertas_ingreso()


# * Ejemplo D: Actualización de Inventario de Souvenirs (Uso de Diccionarios y Listas)
# ? Una función puede alterar dinámicamente colecciones complejas como un inventario de 
# ? tienda de música, combinando diccionarios con listas internas para modificar existencias.
def auditoria_tienda_oficial():
    # * Tipo de dato: Diccionario (dict) con los precios de la mercancía
    precios_productos = {"Polera": 35.0, "Gorra": 20.0, "Poster": 10.5} # str y float
    # * Tipo de dato: Lista (list) con las ventas registradas en la última hora
    ultimas_ventas = ["Polera", "Poster", "Polera"]
    
    print("🛍️ [MERCH] Iniciando cierre de caja rápido de la tienda del concierto...")
    total_recaudado = 0
    for venta in ultimas_ventas:
        total_recaudado += precios_productos[venta]
        print(f"    + Vendido: {venta} (${precios_productos[venta]})")
    print(f"💰 [MERCH] Total recaudado en esta tanda: ${total_recaudado}")

print("\n--- Refuerzo D: Lógica Avanzada con Diccionarios y Listas ---")
auditoria_tienda_oficial()