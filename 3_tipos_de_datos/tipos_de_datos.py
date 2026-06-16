# ==========================================
# 3_tipos_de_datos -> tipos_de_datos.py
# ==========================================

# * 1. TIPO DE DATO BOOLEANO (bool)
# ------------------------------------------
# ? Solo pueden tener dos valores: Verdadero (True) o Falso (False).

# Variables
tiene_computadora = True
esta_lloviendo = False

# Constantes
PERMITIR_MENORES = False
SISTEMA_OPERATIVO_WINDOWS = True


# * 2. TIPO DE DATO ENTERO (int)
# ------------------------------------------
# ? Números completos, positivos o negativos, sin decimales.

# Variables
edad_actual = 21
gatos_en_casa = 2

# ! TIP PROFESIONAL: Python soporta números gigantescos. 
# ! Usamos guiones bajos (_) como separadores de miles para que sea fácil de leer.
# ? Representa el número: 8 mil billones
saldo_banco = 8_000_000_000_000_000 

# Constantes
MESES_DEL_ANIO = 12
HORAS_DEL_DIA = 24


# * 3. TIPO DE DATO FLOTANTE / REAL (float)
# ------------------------------------------
# ? Números que contienen una parte decimal. Se usa el punto (.) como separador.

# Variables
precio_pasaje = 2.50
peso_kilogramos = 68.4

# ! TIP PROFESIONAL: El guion bajo (_) también funciona en decimales de forma libre.
# ? Python ignora los guiones bajos y lee el número de forma corrida.
numero_ultra_preciso = 1_122_234.4554_3434

# Constantes
PI = 3.14159
GRAVEDAD_TIERRA = 9.81


# * 4. TIPO DE DATO CADENA DE TEXTO (str)
# ------------------------------------------
# ? Texto plano. En Python se puede usar comillas dobles (") o simples (').

# Variables
nombre_estudiante = "Katty"
ciudad_origen = 'Cochabamba'
fila_asiento = 'A'          # ? Nota: Un solo carácter sigue siendo tipo 'str' en Python.

# Constantes
PAIS = 'Bolivia'
IDIOMA_PREDETERMINADO = "Español"


# * 5. ¿CÓMO SABER EL TIPO DE DATO DE UNA VARIABLE?
# ------------------------------------------
# ? La función type() nos dice qué tipo de dato almacena la variable en ese momento.

print("El tipo de dato de precio_pasaje es:", type(precio_pasaje))
print("El tipo de dato de nombre_estudiante es:", type(nombre_estudiante))
print("El valor del decimal libre es:", numero_ultra_preciso)
