# ==============================================================================
# # 9_persistencia_con_json -> 1_formato_y_libreria.py
# ==============================================================================

# ==============================================================================
# * INTRODUCCIÓN A LA PERSISTENCIA Y EL FORMATO JSON
# ==============================================================================

# ------------------------------------------------------------------------------
# * 1.1 El Límite de la Memoria RAM vs. El Disco Duro (Persistencia)
# ------------------------------------------------------------------------------

# * Declaramos datos simulados en la memoria RAM de la PC
datos_sesion_ram = {"usuario": "Invitado_99", "modo_oscuro": True, "nivel": 1}

print("--- Estado de los Datos en la RAM ---")
print(f"Información cargada actualmente en la memoria volátil: {datos_sesion_ram}")
# ! NOTA: Si detenemos el script aquí, esta información se desvanecerá para siempre.


# ------------------------------------------------------------------------------
# * 1.2 ¿Qué es el formato JSON y cuál es su estructura?
# ------------------------------------------------------------------------------
# JavaScript Object Notation - JSON

# * Representación visual de cómo luce un texto estructurado en formato JSON:
# {
#     "servidor_nombre": "Servidor_Central",
#     "puertos_abiertos":,
#     "esta_activo": true
# }
# ! NOTA: Observa que es idéntico a un diccionario de Python, con la única diferencia 
# ! de que los booleanos en JSON se escriben estrictamente en minúscula: 'true' o 'false'.

# ------------------------------------------------------------------------------
# * 1.3 La Importación de la Librería Nativa 'json'
# ------------------------------------------------------------------------------

import json

print("\n--- Validación del Entorno de Persistencia ---")
print("Librería oficial de traducción 'json' importada con éxito.")
print("El sistema está preparado para comunicarse con el almacenamiento del disco duro.")