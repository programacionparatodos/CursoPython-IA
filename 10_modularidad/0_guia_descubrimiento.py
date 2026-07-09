# ==============================================================================
# # 10_modularidad -> 0_guia_descubrimiento.py
# ==============================================================================

# ==============================================================================
# * GUÍA DE DESCUBRIMIENTO: ¿QUÉ MÓDULOS EXISTEN Y CÓMO SABER PARA QUÉ SIRVEN?
# ==============================================================================

# ------------------------------------------------------------------------------
# * 0.1 ¿Cómo ver la lista de TODOS los módulos instalados? (`help("modules")`)
# ------------------------------------------------------------------------------

print("--- 0.1 Descubriendo el Catálogo Completo de Python ---")
print("Ejecuta la línea de abajo en tu consola para ver el listado completo:")
# help("modules") # ! NOTA: Está tarda unos segundos en escanear todo.

# ! ALERTA: La lista es gigantesca. No intentes memorizarla. Los programadores 
# ! profesionales solo buscan los módulos cuando los necesitan.

# ------------------------------------------------------------------------------
# * 0.2 El Buscador de Funciones Inteligente (`dir`)
# ------------------------------------------------------------------------------

import math # Importamos para poder inspeccionarlo

print("\n--- 0.2 Inspección de Herramientas Internas con dir() ---")
herramientas_de_math = dir(math)

print(f"El módulo 'math' tiene {len(herramientas_de_math)} herramientas.")
# * Mostramos todas las herramientas del módulo
print(f"Algunas de sus herramientas son: {herramientas_de_math}")

# * Mostramos las primeras 5 herramientas del módulo
print(f"Algunas de sus herramientas son: {herramientas_de_math[:5]}")

# ------------------------------------------------------------------------------
# * 0.3 El Manual de Usuario Integrado (`help`)
# ------------------------------------------------------------------------------

print("\n--- 0.3 Leyendo el Manual Técnico con help() ---")
# * Le pedimos a Python que nos explique para qué sirve la función 'isqrt' de 'math'
help(math.isqrt) 

# ! NOTA: Al pasar la función a 'help()', se pasa SIN los paréntesis finales. 
# ! Usa 'math.isqrt' (correcto) en lugar de 'math.isqrt()' (incorrecto).


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: El "Top 8" de Módulos Nativos más Usados
# ------------------------------------------------------------------------------
# ? A continuación, se presenta un mapa rápido de los módulos que todo estudiante 
# ? principiante debe conocer y el problema exacto que resuelven en el mundo real:

# * 1. Módulo: os (Operating System)
# ? ¿Para qué sirve?: Crear carpetas, borrar archivos y explorar directorios de tu PC.
# import os

# * 2. Módulo: sys (System)
# ? ¿Para qué sirve?: Controlar el intérprete de Python y ver configuraciones del sistema.
# import sys

# * 3. Módulo: random
# ? ¿Para qué sirve?: Generar números aleatorios, juegos de azar o elegir elementos al azar.
# import random

# * 4. Módulo: datetime
# ? ¿Para qué sirve?: Manejar calendarios, calcular días vividos, horas y zonas horarias.
# import datetime

# * 5. Módulo: math
# ? ¿Para qué sirve?: Operaciones matemáticas complejas (trigonometría, logaritmos, etc.).
# import math

# * 6. Módulo: json
# ? ¿Para qué sirve?: Guardar datos de tu programa en archivos de texto estructurados.
# import json

# * 7. Módulo: statistics
# ? ¿Para qué sirve?: Calcular medias, medianas, modas y desviaciones estándar fácilmente.
# import statistics

# * 8. Módulo: urllib (o requests en librerías externas)
# ? ¿Para qué sirve?: Conectarse a internet, leer páginas web y descargar contenido de redes.
# import urllib.request