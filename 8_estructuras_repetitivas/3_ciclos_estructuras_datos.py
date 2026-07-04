# ==============================================================================
# # 8_estructuras_repetitivas -> 3_ciclos_estructuras_datos.py
# ==============================================================================

# ==============================================================================
# * CICLOS Y ESTRUCTURAS DE DATOS: MINI-CRUD INTERACTIVO REAL
# ==============================================================================
#C   create     crear
#R   read       visualizar
#U   update     modificar
#D   delete     eliminar
     #exit      salir

# * Nuestra Base de Datos inicial (Lista que almacena Diccionarios en la memoria RAM)
inventario_sistema = [
    {"id": 1, "nombre": "Auto a Control Remoto", "stock": 12},
    {"id": 2, "nombre": "Muñeca Articulada", "stock": 8},
    {"id": 3, "nombre": "Bloques de Construcción", "stock": 25}
]

print("--- Iniciando Sistema de Gestión de Datos de Consola ---")

# * El Motor Principal: El bucle while True mantiene la aplicación encendida continuamente
while True:
    print("\n==============================")
    print("      MINI-CRUD DE CONTROL    ")
    print("==============================")
    print("1. [CREATE]  Añadir juguete nuevo")
    print("2. [READ]    Visualizar inventario de juguetes")
    print("3. [UPDATE]  Modificar stock de un juguete")
    print("4. [DELETE]  Eliminar un juguete")
    print("5. [EXIT]    Apagar sistema")
    print("==============================")
    
    # * Captura segura como texto para evitar colapsos por ingresos accidentales de letras
    opcion_elegida = input("Seleccione una opción (1-5): ")

    # * Control de flujo principal utilizando la estructura moderna match-case
    match opcion_elegida:

        # ----------------------------------------------------------------------
        # * OPCIÓN 1: CREATE (Añadir elementos dinámicamente)
        # ----------------------------------------------------------------------
        case "1":
            print("\n--- [CREATE] Registrando nuevo juguete ---")
            nuevo_id = int(input("Ingrese el número de ID único para el juguete: "))
            nuevo_nombre = input("Ingrese el nombre del juguete: ")
            nuevo_stock = int(input("Ingrese la cantidad inicial en stock: "))
            
            nuevo_elemento = {"id": nuevo_id, "nombre": nuevo_nombre, "stock": nuevo_stock}
            inventario_sistema.append(nuevo_elemento)
            print(f"¡Éxito! '{nuevo_nombre}' agregado al almacén de la juguetería.")
            
        # ----------------------------------------------------------------------
        # * OPCIÓN 2: READ (Visualizar colecciones con Cláusula de Guarda)
        # ----------------------------------------------------------------------
        case "2":
            print("\n--- [READ] Inventario Completo de la Juguetería ---")
            
            # * CLÁUSULA DE GUARDA: Descartamos el estado de error (lista vacía) de inmediato
            if len(inventario_sistema) == 0:
                print("[AVISO] La tienda está vacía. No hay juguetes en estantería.")
                continue # Salta directo al inicio del menú 'while' evitando ejecutar lo de abajo
            
            # * Camino Feliz: Se ejecuta libremente si la lista tiene elementos
            for item in inventario_sistema:
                print(f"-> ID: {item['id']} | Juguete: {item['nombre']} | Disponibles: {item['stock']} unidades")

        # ----------------------------------------------------------------------
        # * OPCIÓN 3: UPDATE (Modificar datos con Cláusulas de Guarda en bucles)
        # ----------------------------------------------------------------------
        case "3":
            print("\n--- [UPDATE] Modificación de Stock en Tiempo Real ---")
            id_a_buscar = int(input("Ingrese el ID del juguete que desea modificar: "))
            
            # * Extraemos todos los IDs existentes en una lista usando comprensión rápida o ciclo directo
            ids_existentes = [juguete["id"] for juguete in inventario_sistema]
            
            # * CLÁUSULA DE GUARDA: Evaluamos y descartamos el error de inmediato si el ID no existe
            if id_a_buscar not in ids_existentes:
                print(f"[ERROR] El ID {id_a_buscar} no corresponde a ningún juguete en inventario.")
                continue

            # * Camino Feliz: Buscamos el elemento con la seguridad absoluta de que sí está en la lista
            for item in inventario_sistema:
                if item["id"] == id_a_buscar:
                    nuevo_valor_stock = int(input(f"Juguete '{item['nombre']}' localizado. Ingrese el nuevo stock: "))
                    item["stock"] = nuevo_valor_stock
                    print(f"¡Modificado! El juguete '{item['nombre']}' ahora cuenta con {nuevo_valor_stock} unidades.")
                    break

        # ----------------------------------------------------------------------
        # * OPCIÓN 4: DELETE (Eliminar registros usando Cláusula de Guarda)
        # ----------------------------------------------------------------------
        case "4":
            print("\n--- [DELETE] Remoción de Juguetes Definitiva ---")
            id_a_eliminar = int(input("Ingrese el ID del juguete que desea retirar de la tienda: "))
            
            # * Mapeamos los IDs de la base de datos para validar su existencia de forma limpia
            ids_existentes = [juguete["id"] for juguete in inventario_sistema]
            
            # * CLÁUSULA DE GUARDA: Descartamos el error inmediatamente si el ID a borrar no existe
            if id_a_eliminar not in ids_existentes:
                print(f"[ERROR] No se encontró ningún juguete registrado con el ID {id_a_eliminar}.")
                continue

            # * Camino Feliz: Como el ID es válido, lo ubicamos y lo removemos sin rodeos de variables extras
            for item in inventario_sistema:
                if item["id"] == id_a_eliminar:
                    inventario_sistema.remove(item)
                    print(f"¡Eliminado! El juguete '{item['nombre']}' fue retirado del sistema.")
                    break

        # ----------------------------------------------------------------------
        # * OPCIÓN 5: EXIT (Cierre seguro de la aplicación)
        # ----------------------------------------------------------------------
        case "5":
            print("\n[APAGADO] Cerrando el sistema de la tienda. Fin de la ejecución.")
            break
            
        # ----------------------------------------------------------------------
        # * CASO POR DEFECTO: Captura cualquier entrada inválida (números fuera de rango o letras)
        # ----------------------------------------------------------------------
        case _:
            print("[ALERTA] Opción incorrecta. Elija un número válido del 1 al 5.")
        

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Desafío Autónomo para Practicar en Casa
# ------------------------------------------------------------------------------
# * ¡RETO DE CONSOLIDACIÓN!: EL SISTEMA DE EMBARQUE DE "VUELOS-BOLIVIA"
# ------------------------------------------------------------------------------
# ? INSTRUCCIONES PARA EL ESTUDIANTE:
# ? Basándote exactamente en la estructura interactiva de teclado que acabas de ver 
# ? en el código superior, debes programar el prototipo para una aerolínea. 
# ? 
# ? Tu base de datos inicial debe ser una lista con la siguiente estructura:
# ? lista_pasajeros = [
# ?     {"asiento": 12, "nombre": "Mariana Flores", "destino": "Santa Cruz"},
# ?     {"asiento": 25, "nombre": "Alejandro Choque", "destino": "La Paz"}
# ? ]
# ?
# ? REQUISITOS DEL PROGRAMA A CONSTRUIR:
# ? 1. El menú debe repetirse sin apagarse nunca y pedir las opciones por teclado:
# ?    - Opción [A]: Registrar nuevo pasajero (Pidiendo datos por input y usando .append).
# ?    - Opción [B]: Mostrar lista de abordaje (Un ciclo 'for' que imprima los datos).
# ?    - Opción [C]: Cambiar destino de vuelo (Pedir asiento, buscar con 'for' y modificar).
# ?    - Opción [D]: Cancelar pasaje o Salir (Romper el ciclo principal con un 'break').

# print("\n=======================================================")
# TODO: Escribe tu solución aquí abajo usando 'input()' para que sea interactivo.
# TODO: Enviar este archivo al grupo de whatsapp, en el código colocas tu NOMBRE COMPLETO
# print("   [ESPACIO RESERVADO PARA EL CÓDIGO DEL ESTUDIANTE]   ")
# print("=======================================================")
