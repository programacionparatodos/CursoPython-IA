# ==============================================================================
# # 10_modularidad -> 1_modulos_nativos.py
# ==============================================================================

# ==============================================================================
# * MODULARIDAD I: REUTILIZACIÓN DE CÓDIGO Y MÓDULOS NATIVOS (LIBRERÍA ESTÁNDAR)
# ==============================================================================

import math # Importamos el módulo de funciones matemáticas avanzadas

print("--- 1.1 Importación Total ('import') ---")
# * Usamos la función raíz cuadrada (sqrt) anteponiendo el nombre del módulo
resultado_raiz = math.sqrt(64)
print(f"La raíz cuadrada utilizando math de 64 es: {resultado_raiz}")

# ! NOTA: Si intentas escribir 'print(sqrt(64))' directamente sin poner 'math.',
# ! Python arrojará un error 'NameError' porque no sabe de dónde sale esa función.

# * No utilizamos una función pero obtenemos el mismo resultado
resultado_raiz_exponente = 64 ** (1/2)
print(f"La raíz cuadrada sin utilizar math de 64 es: {resultado_raiz_exponente}")

# ------------------------------------------------------------------------------
# * 1.2 Importación con Alias ('import ... as ...')
# ------------------------------------------------------------------------------

import datetime as dt # Renombramos el módulo de fechas y horas a solo 'dt'

print("\n--- 1.2 Importación con Alias ('as') ---")
# * Obtenemos el año actual usando el alias corto
año_actual = dt.datetime.now().year
print(f"Estamos ejecutando este script en el año: {año_actual}")

# ------------------------------------------------------------------------------
# * 1.3 Importación Específica ('from ... import ...')
# ------------------------------------------------------------------------------

from random import randint # Extraemos solo la función para generar enteros aleatorios

print("\n--- 1.3 Importación Específica ('from/import') ---")
# * Usamos la función directamente como si la hubiéramos creado aquí
dado_aleatorio = randint(1, 6)
print(f"Resultado del lanzamiento del dado: {dado_aleatorio}")

# ------------------------------------------------------------------------------
# * 1.4 El peligro de la Importación Masiva ('from ... import *')
# ------------------------------------------------------------------------------
# ? Concepto corto: Trae absolutamente todo el contenido del módulo directamente 
# ? al archivo actual. Está fuertemente desaconsejado en proyectos reales.

from os import * # Trae funciones del Sistema Operativo (¡Peligro latente!)

print("\n--- 1.4 Simulación de Riesgo por Importación Masiva ---")
# * Obtenemos la ruta actual del sistema operativo
ruta_trabajo = getcwd() 
print(f"Ruta actual detectada en el sistema: {ruta_trabajo}")

# ! ALERTA: Si en tu código creas una función que se llame igual a una del módulo 
# ! (por ejemplo, si creas tu propia función llamada 'getcwd'), sobreescribirás 
# ! la original de Python sin darte cuenta, rompiendo tu programa (Colisión de nombres).


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Combinar importación específica con alias personalizado
# ? Puedes extraer una sola función específica de un módulo y ponerle un alias 
# ? único para evitar conflictos con otras variables de tu código.
from time import sleep as pausar_programa
print("\n--- Refuerzo A: Alias en Funciones Específicas ---")
print("Iniciando descarga de datos...")
pausar_programa(1.5) # Detiene la ejecución del código por 1.5 segundos simulados
print("Descarga completada con éxito.")