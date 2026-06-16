# ==========================================
# 4_entrada_salida -> entrada.py
# ==========================================

# ? La función input() SIEMPRE recibe los datos del usuario como texto (str).
# ? Para usar números, debemos transformar el texto mediante 'casting' (conversión).

# * 1. ENTRADA PARA TEXTO (str)
# ------------------------------------------
# ? Al ser texto de forma nativa, no requiere ninguna conversión.
nombre = input("Ingrese su nombre completo: ")
print("El tipo de dato de nombre es:", type(nombre))


# * 2. ENTRADA PARA ENTEROS (int)
# ------------------------------------------
# ? Envolvemos el input() dentro de int() para convertir el texto a número entero.
edad = int(input("Ingrese su edad: "))
print("El tipo de dato de edad es:", type(edad))


# * 3. ENTRADA PARA FLOTANTES / REALES (float)
# ------------------------------------------
# ? Envolvemos el input() dentro de float() para permitir números con decimales.
precio = float(input("Introduce el precio del pasaje: "))
print("El tipo de dato de precio es:", type(precio))


# * 4. ENTRADA PARA BOOLEANOS (bool)
# ------------------------------------------
# ! ALERTA: Hacer bool(input()) no funciona como esperas porque cualquier texto devuelve True.
# ? La forma correcta es capturar el texto y evaluarlo con una condición lógica.
respuesta = input("¿Tienes mascotas? (si/no): ")
tiene_mascota = (respuesta == "si")  # Evalúa a True si escribe exactamente "si", de lo contrario False.

print("¿Tiene mascota?:", tiene_mascota)
print("El tipo de dato de tiene_mascota es:", type(tiene_mascota))
