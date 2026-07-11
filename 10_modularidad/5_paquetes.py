# ==============================================================================
# # 10_modularidad -> 5_paquetes.py
# ==============================================================================

# ==============================================================================
# * MODULARIDAD III: PAQUETES (ORGANIZANDO NUESTROS ARCHIVOS EN CARPETAS)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 5.1 Importar desde una Carpeta usando la ruta del punto (.)
# ------------------------------------------------------------------------------

import clinica_veterinaria.zona_perros

print("--- 5.1 Abriendo Módulos Ocultos dentro de Carpetas ---")
# * Invocamos la función haciendo el recorrido de la ruta completa de carpetas
# * Pasamos datos de tipo: str, int, float y bool
perrito_registrado = clinica_veterinaria.zona_perros.registrar_perro("Rocco", 3, 14.6, True)

print(f"Ficha médica creada en el sistema: {perrito_registrado}")

# ! NOTA: Tener que escribir `clinica_veterinaria.zona_perros.funcion()` en cada 
# ! línea puede volverse sumamente largo, aburrido y difícil de leer.

# ------------------------------------------------------------------------------
# * 5.2 Simplificación de Rutas de Paquetes mediante Alias (`as`)
# ------------------------------------------------------------------------------

import clinica_veterinaria.zona_gatos as quirofano_gatos

print("\n--- 5.2 Uso de Alias para Submódulos de Carpetas ---")
# * Tipo de dato: Diccionario (dict) compuesto con la información del paciente
michi_paciente = {"nombre": "Rosita", "sexo": "hembra", "esta_enfermo": False}

# * Usamos el alias corto del módulo para evaluar al felino
mensaje_salida = quirofano_gatos.dar_alta_gato(michi_paciente)
print(mensaje_salida)

# ------------------------------------------------------------------------------
# * 5.3 Extracción Directa de Herramientas desde un Paquete
# ------------------------------------------------------------------------------

from clinica_veterinaria.zona_perros import inventario_canino

print("\n--- 5.3 Accediendo a Variables y Colecciones de un Paquete ---")
# * Al extraer la colección directamente, podemos leer su estado sin prefijos largos
print(f"Lista de perritos actualmente internados: {inventario_canino['pacientes_actuales']}")


# ------------------------------------------------------------------------------
# * 5.4 El mito del archivo de inicialización `__init__.py`
# ------------------------------------------------------------------------------

print("\n--- 5.4 El Secreto del archivo __init__.py ---")
print("[INFO] En Python 3 (actual), las carpetas normales se reconocen solas.")
print("[INFO] Sin embargo, si creas este archivo, puedes programar mensajes ")
print("[INFO] de bienvenida automáticos al momento de abrir la carpeta.")

# ! ALERTA: Si en el futuro trabajas en una empresa con servidores viejos que usen 
# ! Python 2, si no creas este archivo, tus importaciones de carpetas van a fallar.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Lectura de Constantes Globales de Carpetas (Uso de Tuplas)
# ? Los paquetes pueden almacenar archivos de configuración que guarden tuplas fijos 
# ? con los horarios de atención de la veterinaria para que ningún archivo los altere.
# horario_atencion = ("08:00", "20:00") # tuple de str
# print("\n--- Refuerzo A: Datos Inmutables desde Módulos ---")
# print(f"La clínica atiende estrictamente en el bloque de: {horario_atencion}")


# * Ejemplo B: Evitar Duplicados de Clientes en el Registro (Uso de Sets)
# ? Una función dentro de un paquete puede recibir una lista de nombres de mascotas 
# ? ingresadas en el día y transformarla en un set para saber cuántos dueños únicos asistieron.
# def contar_dueños_unicos(lista_mascotas):
#     # * Eliminamos nombres repetidos convirtiendo la lista a conjunto (set)
#     return len(set(lista_mascotas))
#
# print("\n--- Refuerzo B: Filtrado de Datos en Paquetes ---")
# registro_ingresos = ["Firulais", "Michi", "Firulais", "Lucas"] # list
# total_clientes = contar_dueños_unicos(registro_ingresos)
# print(f"Total de mascotas registradas hoy: {len(registro_ingresos)} | Clientes únicos: {total_clientes}")


# * Ejemplo C: Estructuras de Carpetas Anidadas (Paquetes dentro de paquetes)
# ? Si la veterinaria se convierte en un hospital gigante, puedes meter carpetas 
# ? dentro de otras carpetas. La sintaxis simplemente sigue agregando puntos de ruta.
# # Código teórico de ejemplo:
# # from clinica_veterinaria.historiales.año_2026 import buscar_expediente
# print("\n--- Refuerzo C: Sintaxis de Carpetas Profundas ---")
# print("Para subcarpetas la estructura es: carpeta_madre.subcarpeta.archivo")


# * Ejemplo D: Modificación en Tiempo Real de Diccionarios Externos
# ? Las funciones de tus carpetas pueden alterar diccionarios enteros agregando nuevas 
# ? claves sobre la marcha, como añadir el diagnóstico médico a la ficha de una mascota.
# def añadir_diagnostico(historial_dict, enfermedad_str):
#     historial_dict["diagnostico"] = enfermedad_str
#     historial_dict["bajo_observacion"] = True
#
# print("\n--- Refuerzo D: Mutabilidad de Diccionarios ---")
# ficha_clinica = {"nombre": "Simba", "especie": "Gato"}
# añadir_diagnostico(ficha_clinica, "Resfriado felino leve")
# print(f"Ficha actualizada desde el paquete: {ficha_clinica}")
