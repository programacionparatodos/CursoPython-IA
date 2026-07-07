# ==============================================================================
# # 9_persistencia_con_json -> 3_recuperar_datos.py
# ==============================================================================

# ==============================================================================
# * RECUPERACIÓN DE DATOS (LECTURA FÍSICA Y CLÁUSULAS DE GUARDA)
# ==============================================================================

import json

# ------------------------------------------------------------------------------
# * 3.1 El método open() con el modo de lectura 'r' y la función json.load()
# ------------------------------------------------------------------------------
# ruta_del_archivo = r"C:\Users\ProgramacionParaTodo\Documents\CursoPythonIA\9_persistencia_con_json\registro_inicial.json"

# with open(ruta_del_archivo, "r") as archivo_disco:
#     datos_recuperados = json.load(archivo_disco)

# print(f"Estructura recuperada y revivida en la RAM: {datos_recuperados}")
# print(f"Tipo de estructura recreada: {type(datos_recuperados)}")

# with open("configuracion.json", "r") as archivo_disco:
#     datos_recuperados = json.load(archivo_disco)

# print(f"Estructura recuperada y revivida en la RAM: {datos_recuperados}")
# print(f"Tipo de estructura recreada: {type(datos_recuperados)}")

# ------------------------------------------------------------------------------
# * 3.2 Cláusulas de Guarda con Bloques Try-Except (Blindaje contra archivos inexistentes)
# ------------------------------------------------------------------------------

archivo_fantasma = "partida_guardada.json"

try:
    with open(archivo_fantasma, "r") as archivo_disco:
        datos_partida = json.load(archivo_fantasma)
    print("Archivo cargado sin problemas")
except FileNotFoundError:
    print(f"AVISO DE GUARDA: El archivo {archivo_fantasma} no existe en el disco duro")
    # datos_partida = {"usuario": "Nuevo_Jugador", "puntuacion": 0}