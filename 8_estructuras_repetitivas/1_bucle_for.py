# ==============================================================================
# # 8_estructuras_repetitivas -> 1_bucle_for.py
# ==============================================================================

# ==============================================================================
# * EL BUCLE FOR (ITERACIÓN DEFINIDA Y TÉCNICAS DE RECORRIDO)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 1.1 ¿Qué es el bucle 'for' y forma 1: Recorrido directo por Elementos
# ------------------------------------------------------------------------------

servicios_activos = ["Servidor Web", "Base de Datos", "Servicio DNS"]

print("--- Forma 1: Recorrido Directo por Elemento ---")
for servicio in servicios_activos:
    print(f"Estado del sistema: {servicio} -> Operando correctamente.")

# ------------------------------------------------------------------------------
# * 1.2 Forma 2: Recorrido por Posición o Índices con range() y len()
# ------------------------------------------------------------------------------
print("\n--- Forma 2: Recorrido por Índices (Posición Numérica) ---")
# * range(len(...)) genera una secuencia desde 0 hasta el tamaño de la lista menos 1
for posicion in range(len(servicios_activos)):
    print(f"Índice de memoria [{posicion}] ocupado por el proceso: {servicios_activos[posicion]}")

# ------------------------------------------------------------------------------
# * 1.3 Forma 3: Recorrido simultáneo con la función enumerate()
# ------------------------------------------------------------------------------
print("\n--- Forma 3: Recorrido Completo con Enumerate ---")
# * Desempaquetamos dos variables de control en el mismo ciclo: el índice y el valor
for indice, servicio in enumerate(servicios_activos):
    print(f"Línea de ejecución #{indice + 1}: Analizando el componente '{servicio}'")


# ------------------------------------------------------------------------------
# * 1.4 Forma 4: Recorrido de Diccionarios mediante el método .items()
# ------------------------------------------------------------------------------

config_seguridad = {"firewall": "Activo", "puertos_abiertos": 4, "modo_seguro": False}

print("\n--- Forma 4: Recorrido de Diccionarios (.items) ---")
for parametro, estado in config_seguridad.items():
    print(f"Parámetro de Red -> [{parametro}]: Configurado en '{estado}'")


# for clave in config_seguridad.keys():
#     print(f"Clave: {clave}")


# for valor in config_seguridad.values():
#     print(f"Valor: {valor}")


# ------------------------------------------------------------------------------
# * 1.5 Controladores de Flujo del Ciclo: Las sentencias 'break' y 'continue'
# ------------------------------------------------------------------------------

codigos_procesos = [101, 404, 102, 999, 103]

print("\n--- Control de Flujo: Break y Continue en acción ---")
for codigo in codigos_procesos:
    # * Caso 1: Uso de 'continue' (Saltarse un elemento corrupto o un error)
    if codigo == 404:
        print("[SISTEMA] Código 404 detectado (Error). Saltando elemento sin procesar...")
        continue # Detiene esta vuelta y pasa directo al código 102
        
    # * Caso 2: Uso de 'break' (Detener el sistema ante una amenaza crítica)
    if codigo == 999:
        print("[ALERTA AMENAZA] Código 999 (Intruso). ¡Cierre de emergencia del bucle!")
        break # Cancela el ciclo por completo, el código 103 nunca se leerá
        
    print(f"Ejecutando proceso de usuario legítimo ID: {codigo}")























# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Acumuladores numéricos (Cálculo de pesos totales)
# ? Una técnica clásica consiste en declarar una variable en cero fuera del bucle. 
# ? Al iterar la lista, le vamos sumando el valor de cada elemento consecuentemente.
# pesos_archivos_mb = [120, 45, 300, 15]
# espacio_ocupado = 0 # Variable acumuladora

# for peso in pesos_archivos_mb:
#     espacio_ocupado = espacio_ocupado + peso

# print("\n--- Refuerzo A: Acumulación de Datos ---")
# print(f"El peso total de los archivos analizados es de: {espacio_ocupado} MB")


# * Ejemplo B: Filtrado selectivo combinando For con Condicionales
# ? Podemos evaluar cada elemento dentro del ciclo con un bloque 'if' para ejecutar 
# ? instrucciones únicamente sobre aquellos objetos que cumplan un requisito específico.
# voltajes_linea = [220, 245, 215, 260, 222]

# print("\n--- Refuerzo B: Filtrado en Ciclos ---")
# print("Iniciando escaneo de seguridad en la red eléctrica...")
# for voltaje in voltajes_linea:
#     if voltaje > 230:
#         print(f"[ALERTA CRÍTICA] Sobretensión detectada: ¡{voltaje}V! Regulando sistema.")


# * Ejemplo C: Bucles anidados (Un ciclo dentro de otro ciclo)
# ? Python permite meter un 'for' dentro de las líneas de otro 'for'. El ciclo interno 
# ? dará todas sus vueltas completas por cada una de las vueltas individuales que dé el ciclo externo.
# carpetas = ["Fotos", "Documentos"]
# archivos = ["item_1.dat", "item_2.dat"]

# print("\n--- Refuerzo C: Ciclos Anidados ---")
# print("Escaneando directorios del disco duro:")
# for carpeta in carpetas:
#     print(f"Entrando a la carpeta: /{carpeta}")
#     for archivo in archivos:
#         print(f"  -> Verificando archivo: {archivo}")


# * Ejemplo D: Búsqueda y Validación de banderas (Saber si algo existe)
# ? El ciclo recorre la lista buscando un valor. Si lo encuentra, activa una variable 
# ? booleana (bandera o flag) y corta el ciclo con un 'break' porque ya encontró el objetivo.
# usuarios_bloqueados = ["user33", "spammer9", "hacker_pro", "invitado2"]
# usuario_ingresando = "hacker_pro"
# encontrado = False # Variable bandera

# for usuario in usuarios_bloqueados:
#     if usuario == usuario_ingresando:
#         encontrado = True
#         break # Dejamos de buscar porque ya lo localizamos

# if encontrado:
#     print("\n--- Refuerzo D: Validación de Banderas ---")
#     print(f"[BLOQUEO] Acceso denegado. El usuario '{usuario_ingresando}' está en la lista negra.")