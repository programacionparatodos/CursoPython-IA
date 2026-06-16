# ==========================================
# 1_variables -> variables.py
# ==========================================

# ? Una variable es un espacio en la memoria (como una caja) que almacena un valor.

# * 1. REGLAS DE NOMENCLATURA (PEP 8)
# ------------------------------------------
# * Regla 1: Solo pueden contener letras (A-Z, a-z), dígitos (0-9) y guiones bajos (_).
# * Regla 2: Deben empezar con una letra o un guion bajo (NUNCA con un número).
# * Regla 3: No pueden usar palabras reservadas de Python (como print, if, True).
# ? Consejo: En Python se usa 'snake_case' para nombres largos (ej. mi_variable_nueva).

mi_variable = "Correcto"
_contador = 10          # Correcto
# 1_numero = 5          # ! ERROR: No puede empezar con un número


# * 2. TIPOS DE ASIGNACIÓN
# ------------------------------------------

# * Asignación Simple: Un valor para una variable.
edad = 25
nombre = 'Rene'

# * Asignación Múltiple: Diferentes valores en una sola línea.
base, altura = 10, 20

# * Mismo Valor Múltiple: El mismo dato para varias variables a la vez.
x = y = z = 0


# * 3. ASIGNACIÓN POR VALOR (COPIAR COMPORTAMIENTO)
# ------------------------------------------
# ? Al asignar una variable a otra, se copia su valor actual. No quedan "atadas".

precio_original = 100
precio_final = precio_original   # precio_final copia el 100 actual

# ! CASO CRÍTICO: Modificar la variable original NO altera la copia
precio_original = 150

# ? Usamos comas para mostrar el texto junto al valor de la variable
print("Precio Original actual:", precio_original)  # Muestra: Precio Original actual: 150
print("Precio Final (Copia):", precio_final)       # Muestra: Precio Final (Copia): 100
