# ==============================================================================
# 5_operadores -> 5_1_operadores_aritmeticos.py
# ==============================================================================

# ==========================================
# OPERADORES ARITMÉTICOS EN PYTHON
# ==========================================

# ------------------------------------------
# * EJEMPLOS CON NÚMEROS ENTEROS (int)
# ------------------------------------------
# ? Los enteros no tienen parte decimal. Son ideales para contar elementos.

num_1 = 15
num_2 = 4

# * Suma (+)
suma_int = num_1 + num_2  # Resultado: 19

# * Resta (-)
resta_int = num_1 - num_2  # Resultado: 11

# * Multiplicación (*)
mult_int = num_1 * num_2  # Resultado: 60

# * División Flotante (/)
# ! IMPORTANTE: La división flotante SIEMPRE devuelve un número real (float)
div_float_int = num_1 / num_2  # Resultado: 3.75

# * División Entera (//)
# ? Devuelve solo la parte entera del cociente, truncando los decimales
div_entera_int = num_1 // num_2  # Resultado: 3

# * Módulo (%)
# ? Devuelve el residuo o sobrante de la división entera
modulo_int = num_1 % num_2  # Resultado: 3 (porque 4 * 3 = 12, y faltan 3 para 15)

# * Exponenciación (**)
# ? Eleva el primer número a la potencia del segundo
expo_int = num_2 ** 3  # Resultado: 64 (4 elevado al cubo)



# ------------------------------------------
# * EJEMPLOS CON NÚMEROS REALES (float)
# ------------------------------------------
# ? Los reales manejan precisión decimal. Usaremos formateo para controlar los dígitos.

val_1 = 9.84563
val_2 = 2.12345

# * Suma (+)
suma_float = val_1 + val_2
print(f"Suma con 2 decimales: {suma_float:.2f}")  # Muestra: 11.97

# * Resta (-)
resta_float = val_1 - val_2
print(f"Resta con 4 decimales: {resta_float:.4f}")  # Muestra: 7.7222

# * Multiplicación (*)
mult_float = val_1 * val_2
print(f"Producto con 3 decimales: {mult_float:.3f}")  # Muestra: 20.907

# * División Flotante (/)
div_float = val_1 / val_2
print(f"División real completa: {div_float}")  # Muestra el número largo

# * División Entera (//)
# ! ALERTA: Si usas reales, el resultado es un número real con la parte decimal en .0
div_entera_float = val_1 // val_2
print(f"División entera con float: {div_entera_float}")  # Muestra: 4.0

# * Módulo (%)
modulo_float = val_1 % val_2
print(f"Residuo con 2 decimales: {modulo_float:.2f}")  # Muestra: 1.35

# * Exponenciación (**)
expo_float = val_2 ** 2
print(f"Base real al cuadrado: {expo_float:.2f}")  # Muestra: 4.51




# ==========================================
# * OPERADORES DE ASIGNACIÓN COMPUESTA
# ==========================================
# ? Combinan un operador aritmético con el signo igual (=).
# ? Propósito: Modificar y actualizar el valor de una variable de forma corta y eficiente.

# * 1. Suma Compuesta (+=) -> Usado como CONTADOR o ACUMULADOR
# ? Suma un valor al valor actual de la variable. Es el más utilizado en bucles (loops).
score = 0
score += 10       # score = score + 10 (Resultado: 10)
score += 5        # score = score + 5  (Resultado: 15)

# * 2. Resta Compuesta (-=) -> Usado como DECREMENTO o CUENTA REGRESIVA
# ? Resta un valor al valor actual de la variable.
vidas = 3
vidas -= 1        # vidas = vidas - 1  (Resultado: 2)

# * 3. Multiplicación Compuesta (*=) -> Usado para DUPLICAR o ESCALAR valores
# ? Multiplica el valor actual por el nuevo factor.
salario = 1000
salario *= 1.10   # salario = salario * 1.10 (Incremento del 10%. Resultado: 1100.0)

# * 4. División Flotante Compuesta (/=) -> Usado para REPARTIR o REDUCIR proporciones
# ! ALERTA: Convierte automáticamente la variable a tipo 'float'.
total = 100
total /= 4        # total = total / 4  (Resultado: 25.0)

# * 5. División Entera Compuesta (//=) -> Usado para descartar decimales al dividir
# ? Divide de forma entera y actualiza con el cociente truncado.
pixeles = 1080
pixeles //= 2     # pixeles = pixeles // 2 (Resultado: 540)

# * 6. Módulo Compuesto (%=) -> Usado para patrones cíclicos o verificar residuos
# ? Calcula el residuo de la división y lo asigna a la variable.
numero = 17
numero %= 5       # numero = numero % 5 (Resultado: 2)

# * 7. Exponenciación Compuesta (**=) -> Usado para crecimiento exponencial rápido
# ? Eleva la variable a la potencia indicada.
base = 2
base **= 3        # base = base ** 3   (Resultado: 8)
 




# ==========================================
# ! CONVERSIÓN IMPLÍCITA (COERCIÓN DE TIPOS)
# ==========================================
# ? Ocurre de forma automática cuando operas tipos distintos.
# ? Regla de Python: Convierte el dato de menor precisión al de mayor precisión (bool -> int -> float).

# * 1. Booleano + Entero (bool + int -> int)
# ? True equivale a 1 y False equivale a 0 en operaciones aritméticas.
bool_int = True + 5          # 1 + 5 = 6 (Resultado tipo 'int')
bool_int_2 = False * 10      # 0 * 10 = 0 (Resultado tipo 'int')

# * 2. Booleano + Real (bool + float -> float)
# ? El booleano se convierte a 1.0 o 0.0 para igualar la precisión del float.
bool_float = True + 4.5      # 1.0 + 4.5 = 5.5 (Resultado tipo 'float')

# * 3. Entero + Real (int + float -> float)
# ? El entero se transforma en float para evitar la pérdida de decimales.
int_float = 10 + 2.5         # 10.0 + 2.5 = 12.5 (Resultado tipo 'float')

# * 4. Booleano + Booleano (bool + bool -> int)
# ? Sumar dos booleanos genera un entero, no otro booleano.
bool_bool = True + True      # 1 + 1 = 2 (Resultado tipo 'int')


# ==========================================
# ! ALERTA: ¿QUÉ NO COMPILA AUTOMÁTICAMENTE?
# ==========================================
# ! Python NO realiza conversiones implícitas entre textos (str) y números (int/float).
# ! Intentar esto lanzará un error de tipo (TypeError):

# texto_numero = "Precio: " + 19.99  #  Error: float no se convierte a str automáticamente
# numero_texto = 10 / "2"            #  Error: str no se convierte a int automáticamente