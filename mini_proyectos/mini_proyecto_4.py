# ==============================================================================
# # mini_proyectos -> mini_proyecto_4.py
# ==============================================================================

# ==============================================================================
# * MINI-PROYECTO 4: SIMULADOR DE CARRITO DE COMPRAS PERSISTENTE (E-COMMERCE)
# ==============================================================================
# ? OBJETIVO: Construir una aplicación interactiva que simule el motor de compras
# ? de una tienda en línea. El sistema permitirá gestionar un carrito en la RAM,
# ? calcular totales aplicando descuentos por volumen de compra y, lo más importante,
# ? salvará los datos en un archivo JSON local para evitar la pérdida de información.

# * [TEMA 9]: IMPORTACIÓN DE LIBRERÍAS DE PERSISTENCIA
import json

# * [TEMA 7]: ESTRUCTURAS DE DATOS (EL CATÁLOGO DE LA TIENDA)
# ? Usamos una Lista que anida Diccionarios estáticos para modelar los artículos disponibles
CATALOGO_PRODUCTOS = [
    {"id": 101, "nombre": "Teclado Mecánico RGB", "precio": 450},
    {"id": 102, "nombre": "Mouse Gamer Óptico", "precio": 250},
    {"id": 103, "nombre": "Monitor Gamer 24' 144Hz", "precio": 1350},
    {"id": 104, "nombre": "Audífonos HyperX Cloud", "precio": 520}
]

# * [TEMA 7]: ESTRUCTURA RAÍZ DINÁMICA (EL CARRITO VACÍO)
# ? Creamos la lista que albergará los diccionarios de las compras del cliente en la RAM
carrito_compras = []

# * Nombre del archivo físico permanente en el disco duro
ARCHIVO_PERSISTENCIA = "carrito_abandonado.json"

# ==============================================================================
# * FASE 1: RECONEXIÓN Y RESTAURACIÓN DEL ESTADO (AL INICIAR EL SOFTWARE)
# ==============================================================================
# * [TEMA 9]: BLINDAJE DEFENSIVO Y CLÁUSULA DE GUARDA CON TRY-EXCEPT
try:
    # ? Intentamos abrir el archivo de respaldo en modo lectura ("r")
    with open(ARCHIVO_PERSISTENCIA, "r") as archivo_disco:
        # * [TEMA 9]: FUNCIÓN JSON.LOAD() PARA RESUCITAR DATOS
        carrito_compras = json.load(archivo_disco)
    print("======================================================================")
    print(f"🌟 [SISTEMA]: ¡Bienvenido de vuelta! Restauramos tu carrito del disco.")
    print("======================================================================")
except FileNotFoundError:
    # ? Si el archivo no existe (primera ejecución), descartamos el error pacíficamente
    print("======================================================================")
    print("🚀 [SISTEMA]: Inicializando nueva sesión de compras en la memoria RAM.")
    print("======================================================================")
# ==============================================================================
# * FASE 2: MOTOR DE INTERACCIÓN CONTINUA (EL MENÚ PRINCIPAL)
# ==============================================================================
# * [TEMA 8]: ITERACIÓN INDEFINIDA MEDIANTE BUCLE 'WHILE TRUE'
while True:
    print("\n==========================================")
    print("      TIENDA EN LÍNEA: INTERACTIVA        ")
    print("==========================================")
    print("1. Ver catálogo de productos disponibles")
    print("2. Añadir un artículo al carrito de compras")
    print("3. Ver mi carrito actual y calcular el total")
    print("4. Eliminar un artículo específico del carrito")
    print("5. Vaciar por completo el carrito de compras")
    print("6. Salir y guardar mis compras de forma segura")
    print("==========================================")
    
    # * [TEMA 8]: CAPTURA SEGURA EN TEXTO (STR) CONTRA COLAPSOS POR LETRAS
    entrada_usuario = input("Seleccione una opción de control (1-6): ")

    # * [TEMA 8]: 🛡️ CLÁUSULA DE GUARDA UTILIZANDO EL MÉTODO .ISDIGIT()
    if not entrada_usuario.isdigit():
        print("[ALERTA]: Entrada inválida. Debe teclear estrictamente un número entero.")
        continue # Salta de inmediato al inicio del bucle 'while' reiniciando el menú

    # * [TEMA 6]: CAMINO FELIZ (CONVERSIÓN SEGURA A INT TRAS PASAR EL FILTRO)
    opcion_elegida = int(entrada_usuario)

    # * [TEMA 8]: ESTRUCTURA MODERNA DE COINCIDENCIA MATCH-CASE
    match opcion_elegida:

        # ----------------------------------------------------------------------
        # * CASE 1: [READ] VISUALIZAR EL CATÁLOGO DISPONIBLE
        # ----------------------------------------------------------------------
        case 1:
            print("\n--- CATÁLOGO DE PRODUCTOS EN TIENDA ---")
            # * [TEMA 8]: BUCLE 'FOR' PARA RECORRER ESTRUCTURAS ANIDADAS (LISTA DE DICCIONARIOS)
            for producto in CATALOGO_PRODUCTOS:
                print(f"ID: {producto['id']} | {producto['nombre']} | Precio: {producto['precio']} Bs.")

        # ----------------------------------------------------------------------
        # * CASE 2: [CREATE] INYECTAR PRODUCTOS AL CARRITO DINÁMICAMENTE
        # ----------------------------------------------------------------------
        case 2:
            print("\n--- AÑADIR PRODUCTO AL CARRITO ---")
            entrada_id = input("Ingrese el ID del artículo que desea comprar: ")
            
            # * 🛡️ CLÁUSULA DE GUARDA: Validamos que el ID sea numérico
            if not entrada_id.isdigit():
                print("[ERROR]: El ID ingresado debe contener únicamente números.")
                continue
                
            id_a_buscar = int(entrada_id)
            
            # * [TEMA 8]: EXTRACCIÓN RÁPIDA DE IDS PARA VALIDACIÓN COMPUESTA
            ids_catalogo = [p["id"] for p in CATALOGO_PRODUCTOS]
            
            # * 🛡️ CLÁUSULA DE GUARDA: Evaluamos de inmediato si el ID NO pertenece a la tienda
            if id_a_buscar not in ids_catalogo:
                print(f"[ERROR]: El ID {id_a_buscar} no corresponde a ningún producto en catálogo.")
                continue

            # * Camino Feliz: Localizamos el diccionario en el catálogo y lo clonamos al carrito
            for producto in CATALOGO_PRODUCTOS:
                if producto["id"] == id_a_buscar:
                    # * [TEMA 7]: MÉTODO .APPEND() PARA AGRANDAR LA LISTA EN LA RAM
                    carrito_compras.append(producto)
                    print(f"¡Éxito! '{producto['nombre']}' fue añadido a tu carrito.")
                    break

        # ----------------------------------------------------------------------
        # * CASE 3: [READ + LÓGICA] VISUALIZAR EL CARRITO Y TOTALIZAR
        # ----------------------------------------------------------------------
        case 3:
            print("\n--- TU CARRITO DE COMPRAS ACTUAL ---")
            
            # * 🛡️ CLÁUSULA DE GUARDA: Descartamos el procesamiento si el carrito no tiene elementos
            if len(carrito_compras) == 0:
                print("[AVISO]: Tu carrito está completamente vacío. ¡Ve a comprar algo!")
                continue

            # * [TEMA 8]: VARIABLE ACUMULADORA FUERA DEL CICLO (INICIALIZADOR EN CERO)
            subtotal = 0
            
            # * Camino Feliz: Recorremos el carrito acumulando los precios individuales
            for item in carrito_compras:
                print(f"{item['nombre']} | Precio: {item['precio']} Bs.")
                subtotal = subtotal + item["precio"] # Sumador secuencial

            print(f"------------------------------------------")
            print(f"Subtotal acumulado: {subtotal} Bs.")

            # * [TEMA 6 / TEMA 8]: INTEGRACIÓN DE CONDICIONALES DE NEGOCIO (DESCUENTOS)
            # ? Aplicamos la regla comercial: Si el cliente lleva MÁS de 2 productos, se aplica un 10% de descuento.
            if len(carrito_compras) > 2:
                descuento = subtotal * 0.10
                total_final = subtotal - descuento
                print(f"¡Descuento por Volumen Aplicado! (10%): -{descuento:.2f} Bs.")
                print(f"🔥 TOTAL DEFINITIVO A PAGAR: {total_final:.2f} Bs.")
            else:
                print(f"🚨 TOTAL DEFINITIVO A PAGAR: {subtotal} Bs.")
                print("[INFO]: Lleva más de 2 productos en tu próxima compra para activar un 10% de descuento.")
        # ----------------------------------------------------------------------
        # * CASE 4: [DELETE] REMOVER UN ARTÍCULO ESPECÍFICO DEL CARRITO
        # ----------------------------------------------------------------------
        case 4:
            print("\n--- ELIMINAR ARTÍCULO DEL CARRITO ---")
            
            # * 🛡️ CLÁUSULA DE GUARDA: No podemos borrar nada si la lista ya está vacía
            if len(carrito_compras) == 0:
                print("[ERROR]: No tienes ningún elemento en el carrito para dar de baja.")
                continue

            entrada_id_borrar = input("Ingrese el ID del artículo que desea retirar de sus compras: ")
            
            if not entrada_id_borrar.isdigit():
                print("[ERROR]: El ID de eliminación debe ser numérico.")
                continue
                
            id_a_eliminar = int(entrada_id_borrar)
            
            # * Mapeamos los IDs presentes únicamente dentro del carrito actual
            ids_en_carrito = [item["id"] for item in carrito_compras]

            # * 🛡️ CLÁUSULA DE GUARDA: Descartamos la acción si el ID ingresado no está en el carrito
            if id_a_eliminar not in ids_en_carrito:
                print(f"[ERROR]: El ID {id_a_eliminar} no se encuentra dentro de tu carrito de compras.")
                continue

            # * Camino Feliz: Recorremos la estructura buscando el elemento para clausurarlo
            for item in carrito_compras:
                if item["id"] == id_a_eliminar:
                    # * [TEMA 7]: MÉTODO .REMOVE() EXCLUSIVO PARA EXTRAER EL OBJETO DE LA LISTA
                    carrito_compras.remove(item)
                    print(f"¡Removido! El producto '{item['nombre']}' fue sacado de la lista de compras.")
                    break

        # ----------------------------------------------------------------------
        # * CASE 5: [DELETE TOTAL] VACIAR POR COMPLETO EL CARRITO
        # ----------------------------------------------------------------------
        case 5:
            print("\n--- LIMPIEZA COMPLETA DEL CARRITO ---")
            
            # * 🛡️ CLÁUSULA DE GUARDA: Evaluamos si ya está limpio para no sobre-procesar
            if len(carrito_compras) == 0:
                print("[AVISO]: El carrito ya se encuentra totalmente limpio y vacío.")
                continue
                
            # * [TEMA 7]: MÉTODO .CLEAR() PARA RESETEAR LA COLA DE COMPRAS A CERO ELEMENTOS
            carrito_compras.clear()
            print("💥 ¡Carrito vaciado con éxito! Todos los artículos fueron removidos de la memoria RAM.")

        # ----------------------------------------------------------------------
        # * CASE 6: [PERSISTENCIA FÍSICA] GUARDAR DATOS EN EL DISCO Y APAGAR SOFTWARE
        # ----------------------------------------------------------------------
        case 6:
            print("\n--- CONFIGURANDO PERSISTENCIA DE DATOS DE COMPRA ---")
            print("Escribiendo el archivo físico en el almacenamiento local del sistema...")
            
            # * [TEMA 9]: ANATOMÍA PROFESIONAL DE ESCRITURA MEDIANTE 'WITH OPEN' Y MODO 'W'
            # ? 'with' gestiona el Contexto de memoria garantizando el cierre forzoso del archivo al finalizar.
            # ? 'as' crea el alias temporal de acceso ('archivo_disco_json').
            with open(ARCHIVO_PERSISTENCIA, "w") as archivo_disco_json:
                # * [TEMA 9]: FUNCIÓN JSON.DUMP() PARA INYECTAR LA LISTA DE DICCIONARIOS DE FORMA PERMANENTE
                json.dump(carrito_compras, archivo_disco_json)
                
            print("======================================================================")
            print("💾 [CONSOLIDADO]: Tus compras han sido resguardadas en el Disco Duro.")
            print("👋 [APAGADO]: Cerrando el motor interactivo de la tienda. ¡Vuelve pronto!")
            print("======================================================================")
            break # * [TEMA 8]: SENTENCIA BREAK PARA MATAR EL BUCLE PRINCIPAL 'WHILE TRUE'

        # ----------------------------------------------------------------------
        # * CASE _: COINCIDENCIA POR DEFECTO PARA ENTRADAS FUERA DE RANGO
        # ----------------------------------------------------------------------
        case _:
            print("[ALERTA]: Opción incorrecta. Por favor elija un número entero válido del 1 al 6.")



