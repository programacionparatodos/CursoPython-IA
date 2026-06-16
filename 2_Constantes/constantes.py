# ==========================================
# 2_constantes -> constantes.py
# ==========================================

# ? Una constante es un valor que se define al inicio y NUNCA debería cambiar.
# ! IMPORTANTE: En Python NO existen las constantes reales a nivel de código.
# ? Todo es una CONVENCIÓN (regla de respeto) entre programadores.

# * 1. REGLA DE ESCRITURA (UPPER_CASE)
# ------------------------------------------
# * Regla: Se escriben TOTALMENTE EN MAYÚSCULAS para diferenciarlas de las variables.
# * Si tiene más de una palabra, se separan con guion bajo (ej. PI_MAXIMO).
# * Heredan las mismas reglas de caracteres que las variables (letras, números, _).

PI = 3.14159
GRAVEDAD = 9.81
PRECIO_DOLAR = 42.50


# * 2. EL CONTRATO SOCIAL DEL PROGRAMADOR
# ------------------------------------------
# ? Al ver una variable en mayúsculas, el equipo sabe que NO debe modificar su valor.

# ! Alerta: Técnicamente Python te permite cambiar el valor, pero es una MALA PRÁCTICA.
GRAVEDAD = 10.5  # ¡Mal! Python no dará error, pero rompe la lógica del programa.


# * 3. EJEMPLO DE USO CORRECTO
# ------------------------------------------
# ? Las constantes nos ayudan a evitar usar "números mágicos" sueltos en el código.

precio_producto = 100

# Usamos la constante para calcular el costo total de forma clara
costo_con_dolar = precio_producto * PRECIO_DOLAR

print("Costo del producto en pesos:", costo_con_dolar)
