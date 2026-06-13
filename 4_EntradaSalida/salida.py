# Salida de datos (print)

nombre = "Luna"
edad = 5

# 1. f-strings (La moderna y recomendada)
print(f"Mi mascota se llama {nombre} y tiene {edad} años.")

# 2. Por comas (Separación automática)
print("Mi mascota se llama", nombre, "y tiene", edad, "años.")

# 3. Por concatenación (Operador +)
print("Mi mascota se llama " + nombre + " y tiene " + str(edad) + " años.")

# 4. Método .format() 
print("Mi mascota se llama {} y tiene {} años.".format(nombre, edad))