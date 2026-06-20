# ==============================================================================
# # 5_operadores -> 5_3_operadores_comparacion.py
# ==============================================================================

# ==============================================================================
# * SECCIÓN 1: OPERADORES DE COMPARACIÓN
# ==============================================================================

# ------------------------------------------------------------------------------
# * 1.1 Comprobando Igualdad y Diferencia Absoluta (== / !=)
# ------------------------------------------------------------------------------
# ? El usuario quiere ver una película específica y el sistema valida su ticket
pelicula_ticket = "Súper Mario Galaxy"
pelicula_en_pantalla = "Súper Mario Galaxy"

# * Comprobamos si la película del boleto coincide exactamente con la sala
print("¿Es la película correcta para esta sala?:", pelicula_ticket == pelicula_en_pantalla)

# ? El sistema verifica si el usuario se equivocó de asiento
asiento_reservado = "A-12"
asiento_ocupado = "B-14"

# * Comprobamos si son distintos para lanzar una alerta de reubicación
print("¿El cliente se sentó en un asiento diferente?:", asiento_ocupado != asiento_reservado) 

# ------------------------------------------------------------------------------
# * 1.2 Evaluando Rangos Numéricos (<, >, <=, >=)
# ------------------------------------------------------------------------------
# ? Control de acceso en la taquilla del cine según la edad del cliente
edad_cliente = 15
edad_minima_pelicula = 18

# * Menor que (<) y Mayor o igual que (>=)
# ! ALERTA: Si el cliente no cumple la edad, el sistema bloqueará la venta del boleto
print("¿El cliente es menor de la edad requerida?:", edad_cliente < edad_minima_pelicula) 

print("¿El cliente tiene acceso autorizado por edad?:", edad_cliente >= edad_minima_pelicula) 

# TODO: Recordar que el operador '==' compara valor, no confundir con el '=' de asignación.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa
# ------------------------------------------------------------------------------

# * Ejemplo A: Comparación de cadenas con espacios invisibles (El error oculto)
# ? Los espacios en blanco cuentan como caracteres. Un error tipográfico puede arruinar la validación.
pelicula_base_datos = "Avatar"
entrada_usuario = "Avatar "  # ! Ojo: Tiene un espacio al final

print("¿Coinciden los nombres de la película?:", entrada_usuario == pelicula_base_datos) 
# Muestra: False
print("Solución Profesional usando .strip():", entrada_usuario.strip() == pelicula_base_datos) 
# Muestra: True

# * Ejemplo B: El impacto de la sensibilidad a mayúsculas (Case Sensitive)
# ? Para Python, "M" y "m" son totalmente diferentes debido a sus valores en el código ASCII.
sala_ticket = "VIP"
sala_letrero = "vip"

print("¿El ticket coincide con el letrero de la sala?:", sala_ticket == sala_letrero) # Muestra: False
print("Solución Profesional usando .upper():", sala_ticket == sala_letrero.upper()) # Muestra: True

# * Ejemplo C: La trampa de comparar números guardados como texto (Strings)
# ? Si un número viene desde un input() o base de datos como string, la comparación numérica fallará.
asientos_disponibles = 50
solicitud_boletos = "5"  # Viene como texto

# print(asientos_disponibles >= solicitud_boletos) # ❌ Esto lanzará un TypeError en Python
print("Solución Correcta convirtiendo con int():", asientos_disponibles >= int(solicitud_boletos)) 
# Muestra: True