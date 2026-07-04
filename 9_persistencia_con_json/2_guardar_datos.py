# ==============================================================================
# # 9_persistencia_con_json -> 2_guardar_datos.py
# ==============================================================================

# ==============================================================================
# * GUARDADO DE DATOS (ESCRITURA FÍSICA EN EL DISCO DURO)
# ==============================================================================

import json

# ------------------------------------------------------------------------------
# * 2.1 Desarmando la Sintaxis de Persistencia: 'with', 'open()' y 'as'
# ------------------------------------------------------------------------------
# * with        ->      Palabra clave que garantiza el cierre seguro y automático del archivo
# * open()      ->      Función que busca o crea el archivo. Modo "w" significa (Write/Escribir)
# * as          ->      Conector que asigna un nombre temporal al archivo abierto
# * archivo_texto   ->      Nombre de la variable local que representa al archivo físico
print("--- 2.1: Análisis de Sintaxis y Creación de Archivo Plano Especificando Ruta---")
# ruta_destino = r"C:\Users\ProgramacionParaTodo\Documents\CursoPythonIA\9_persistencia_con_json\registro_inicial.txt"

# with open(ruta_destino, "w") as archivo_texto:
#     archivo_texto.write("Sistema de persistencia activado en el disco duro especificando una ruta")

print("--- 2.1: Análisis de Sintaxis y Creación de Archivo Plano ---")
# with open("registro_inicial.txt", "w") as archivo_texto:
      # * Usamos el alias 'archivo_texto' para ordenar la escritura física en el disco duro
#     archivo_texto.write("Sistema de persistencia activado en el disco duro")

# print("Archivo registro_inicial.txt guardado con éxito")


# ------------------------------------------------------------------------------
# * 2.2 La instrucción json.dump() para exportar Estructuras de Datos
# ------------------------------------------------------------------------------


# * Diccionario en la memoria RAM que representa los ajustes elegidos por un usuario
ajustes_aplicacion = {
    "volumen_musica": 75,
    "pantalla_completa": False,
    "idioma_interfaz": "Español"
}

print("\n--- 2.2: Exportación de Estructuras Complejas con JSON ---")
print(f"Estructura original en la memoria RAM (Volátil): {ajustes_aplicacion}")

# * Aplicamos la sintaxis aprendida: abrimos en modo escritura ("w") y asignamos el alias 'archivo_disco'
with open("configuracion.json", "w") as archivo_disco:
    # * Traducimos el diccionario de la RAM y lo inyectamos directamente al archivo físico
    json.dump(ajustes_aplicacion, archivo_disco)

print("¡Éxito absoluto! Los datos complejos han sido guardados en 'configuracion.json'.")
print("Puedes cerrar la consola con total seguridad; tus datos ya no se perderán.")

# TODO: Nota para el profesor: Muestre a los alumnos que en la barra lateral de VS Code 
# TODO: acaban de aparecer dos archivos reales: 'registro_inicial.txt' y 'configuracion.json'.
# TODO: Ábralos con ellos en vivo para que verifiquen que la información quedó escrita.

