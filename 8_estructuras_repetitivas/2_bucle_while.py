# ==============================================================================
# # 8_estructuras_repetitivas -> 2_bucle_while.py
# ==============================================================================

# ==============================================================================
# * EL BUCLE WHILE (ITERACIÓN INDEFINIDA Y MENÚS DE CONTROL)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 ¿Qué es el bucle 'while' y cuál es su sintaxis básica?
# ------------------------------------------------------------------------------

# * Ejemplo básico: Un contador de intentos de inicio de sesión
print("--- Inicialización del Bucle While ---")
# * El bucle se ejecutará mientras el valor de intentos sea menor o igual a 3
while intentos <= 3:
    print(f"[LOGIN] Validando credenciales... Intento número {intentos}")
    intentos = intentos + 1 # ! CRUCIAL: Modificamos la variable para acercarnos al final
print(intentos)
# ! NOTA: Si olvidas la línea 'intentos = intentos + 1', la variable siempre valdrá 1, 
# ! la condición siempre será verdadera y el programa se quedará congelado para siempre.


# ------------------------------------------------------------------------------
# * 2.2 El peligro del Bucle Infinito y la ausencia de Do-While en Python
# ------------------------------------------------------------------------------

# * Creamos un bucle infinito intencional. Solo morirá si el usuario lo rompe desde adentro.
print("\n--- Simulación de Menú Continuo (Estilo Do-While) ---")
# * Creamos un bucle infinito intencional. Solo morirá si el usuario lo rompe desde adentro.
while True:
    print("\n[MENÚ DE SEGURIDAD]")
    print("1. Analizar sistema")
    print("2. Apagar consola (Salir)")
    
    opcion = "2" # Simulamos que el usuario teclea la opción 2 de inmediato
    print(f"El usuario eligió la opción: {opcion}")
    
    if opcion == "1":
        print("-> Ejecutando antivirus en segundo plano...")
    elif opcion == "2":
        print("-> Cerrando sesión de forma segura. ¡Adiós!")
        break # * Rompe el 'while True' de forma inmediata y salta afuera
    else:
        print("[ERROR] Opción inválida. Intente de nuevo.")



# ------------------------------------------------------------------------------
# * 2.3 Recorrido manual de Listas con un ciclo While
# ------------------------------------------------------------------------------

particiones_disco = ["Disco_C", "Disco_D", "Disco_E"]
indice_manual = 0

print("\n--- Recorrido Manual de Colecciones con While ---")
# * Iteramos mientras nuestro índice manual sea menor a la cantidad de elementos (3)
while indice_manual < len(particiones_disco):
    print(f"Montando volumen de almacenamiento: {particiones_disco[indice_manual]}")
    indice_manual = indice_manual + 1 # Avanzamos manualmente al siguiente vagón



# ------------------------------------------------------------------------------
# * 2.4 Recorrido de Diccionarios con un ciclo While (El truco de conversión)
# ------------------------------------------------------------------------------

config_usuario = {"nombre": "Admin", "idioma": "ES", "nivel": 5}

# * Convertimos las claves del diccionario en una lista real para poder contarlas
lista_claves = list(config_usuario.keys()) # Da como resultado: ["nombre", "idioma", "nivel"]
puntero = 0

print("\n--- Recorrido Especial de Diccionarios con While ---")
# * Iteramos mientras el puntero sea menor a la cantidad de claves (3)
while puntero < len(lista_claves):
    # * Extraemos la clave de la lista según la posición del puntero
    clave_actual = lista_claves[puntero]
    
    # * Usamos esa clave para sacar el valor real desde el diccionario original
    valor_actual = config_usuario[clave_actual]
    
    print(f"Propiedad del Perfil -> {clave_actual}: {valor_actual}")
    puntero = puntero + 1 # Avanzamos manualmente al siguiente elemento

# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Validación estricta de entradas del usuario (Inputs correctos)
# ? Un uso fundamental del 'while' es obligar al usuario a introducir un dato válido. 
# ? Si el usuario se equivoca, el bucle lo regresa al inicio y no lo deja avanzar en el programa.
# print("\n--- Refuerzo A: Validación de Datos ---")
# while True:
#     confirmacion = "SI" # Simulación de entrada de consola
#     if confirmacion == "SI" or confirmacion == "NO":
#         print(f"Entrada aceptada con éxito: {confirmacion}")
#         break
#     print("[ERROR] Respuesta inválida. Escriba estrictamente 'SI' o 'NO'.")


# * Ejemplo B: Uso de Banderas Booleanas (Flags) para controlar el While
# ? En lugar de usar 'break', puedes controlar la vida del bucle utilizando una variable 
# ? booleana. El bucle corre mientras la bandera esté encendida, y se apaga al cambiar su estado.
# sistema_operativo_corriendo = True
# ciclos_reloj = 0

# print("\n--- Refuerzo B: Control con Banderas (Flags) ---")
# while sistema_operativo_corriendo:
#     ciclos_reloj = ciclos_reloj + 1
#     print(f"Procesador ejecutando tareas ocultas... Ciclo: {ciclos_reloj}")
    
#     if ciclos_reloj >= 2:
#         print("[SISTEMA] Temporizador cumplido. Apagando bandera de ejecución.")
#         sistema_operativo_corriendo = False # Al cambiar a False, la siguiente vuelta no se dará


# * Ejemplo C: Saltarse vueltas en un bucle While mediante 'continue'
# ? Al usar 'continue' en un 'while', debes tener un cuidado extremo: debes incrementar 
# ? el contador ANTES del 'continue'; de lo contrario, el programa se quedará atrapado en un bucle infinito.
# contador = 0

# print("\n--- Refuerzo C: Continue en Bucles While ---")
# while contador < 3:
#     contador = contador + 1
#     if contador == 2:
#         print(f"-> Encontrado elemento {contador} en mantenimiento. Saltando...")
#         continue # Salta directo a la línea del 'while contador < 3'
#     print(f"Procesando paquete de datos ID: {contador}")


# * Ejemplo D: Vaciado secuencial de estructuras dinámicas
# ? Podemos usar un 'while' combinado con el método '.pop()' de las listas para ir 
# ? extrayendo y eliminando elementos uno a uno hasta que la lista se quede con tamaño cero.
# cola_descargas = ["parche_1.exe", "parche_2.exe"]

# print("\n--- Refuerzo D: Vaciado de Listas en Tiempo Real ---")
# * En Python, una lista con elementos equivale a True, y una lista vacía equivale a False
# while cola_descargas:
#     archivo_actual = cola_descargas.pop(0) # Extrae el primer elemento
#     print(f"Descargando archivo localmente: {archivo_actual}")

# print(f"Estado final de la cola de descargas: {cola_descargas} (Vacía)")
