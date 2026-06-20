# ==============================================================================
# mini_proyectos -> mini_proyecto_2.py
# ==============================================================================

# ==============================================================================
# # MINIPROYECTO 2: CALCULADORA DE COMPATIBILIDAD DE AVENGERS
# ==============================================================================

print("--------------------------------------------------")
print("       CALCULADORA DE AMISTAD Y COMPATIBILIDAD    ")
print("--------------------------------------------------")

# # --- 1. ENTRADA DE DATOS ---
nombre_persona1 = input("Introduce el primer nombre: ")
nombre_persona2 = input("Introduce el segundo nombre: ")

# # --- 2. LIMPIEZA DE DATOS (.strip() y .upper()) ---
# * Limpiamos los espacios de los extremos y pasamos todo a mayúsculas
n1_limpio = nombre_persona1.strip().upper()
n2_limpio = nombre_persona2.strip().upper()

# # --- 3. COMBINACIÓN DE CADENAS (f-strings) ---
# * Juntamos ambos nombres limpios usando una f-string épica
nombres_combinados = f"{n1_limpio} VS {n2_limpio}"

# # --- 4. OPERACIONES CON TEXTO (.count()) ---
# ? Contamos cuántas letras en total coinciden con la palabra 'AMOR'
letras_amor = (
    nombres_combinados.count("A") +
    nombres_combinados.count("M") +
    nombres_combinados.count("O") +
    nombres_combinados.count("R")
)

# ? Contamos cuántas letras en total coinciden con la palabra 'VERDADERO'
letras_verdadero = (
    nombres_combinados.count("V") +
    nombres_combinados.count("E") +
    nombres_combinados.count("R") +
    nombres_combinados.count("D") +
    nombres_combinados.count("A") +
    nombres_combinados.count("O")
)

# # --- 5. APLICACIÓN DE MATEMÁTICAS (Enteros, Reales y Operadores) ---
# * Calculamos el total de letras que tienen ambos nombres sumados (Uso de len())
total_letras_nombres = len(n1_limpio) + len(n2_limpio)

# * Calculamos los puntos totales acumulados
puntos_totales = letras_amor + letras_verdadero

# ! OPERACIONES CON NÚMEROS REALES (Floats) Y ARITMÉTICA
# ? Para hallar el porcentaje real, dividimos los puntos entre el total de letras.
# ? Multiplicamos por 100 para volverlo porcentaje y usamos la división entera (//)
# ? para que nos devuelva un número entero limpio y no pase de 100 con el operador residuo (%)
porcentaje_calculado = (puntos_totales * 100) // total_letras_nombres

# ! CONTROL DE LÍMITE (Operador de asignación y comparación lógica básica)
# ? Si por alguna razón supera el 100%, lo limitamos matemáticamente usando el operador residuo
porcentaje_final = porcentaje_calculado % 101

# ==============================================================================
# # IMPRESIÓN DEL RESUTADO FINAL
# ==============================================================================
print("\n--------------------------------------------------")
print("             VERDICTO DE COMPATIBILIDAD           ")
print("--------------------------------------------------")
print(f"Nombres evaluados     : {nombres_combinados}")
print(f"Letras 'AMOR' halladas : {letras_amor}")
print(f"Letras 'VERDADERO'    : {letras_verdadero}")
print(f"Total letras base     : {total_letras_nombres} (Número Entero)")
print(f"Puntos / Letras (Real) : {puntos_totales / total_letras_nombres:.2f} (Número Decimal)")
print(f"PORCENTAJE REAL MATEMÁTICO: {porcentaje_final}%")
print("--------------------------------------------------")
