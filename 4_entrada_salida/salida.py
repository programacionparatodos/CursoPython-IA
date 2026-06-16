# ==========================================
# 4_entrada_salida -> salida.py
# ==========================================

# ? La función print() se usa para mostrar información en la consola.
# ? Existen diferentes formas de estructurar y formatear el texto de salida.

nombre = "Luna"
edad = 5

# * 1. F-STRINGS (La moderna y recomendada)
# ------------------------------------------
# ? Es la forma más limpia, legible y eficiente en Python moderno.
# ? Se coloca una 'f' antes de las comillas y las variables van entre llaves {}.
print(f"Mi mascota se llama {nombre} y tiene {edad} años.")


# * 2. POR COMAS (Separación automática)
# ------------------------------------------
# ? Agrega un espacio en blanco de forma automática entre cada elemento.
# ? Permite mezclar textos y números sin necesidad de hacer conversiones manuales.
print("Mi mascota se llama", nombre, "y tiene", edad, "años.")


# * 3. POR CONCATENACIÓN (Operador +)
# ------------------------------------------
# ! ALERTA: Une los textos de forma estricta sin agregar espacios automáticos.
# ! Exige convertir obligatoriamente los números a texto usando str(), si no dará error.
print("Mi mascota se llama " + nombre + " y tiene " + str(edad) + " años.")


# * 4. MÉTODO .FORMAT() (Formato clásico)
# ------------------------------------------
# ? Reemplaza las llaves {} por los valores pasados en orden dentro de .format().
# ? Era la forma estándar antes de que existieran las f-strings.
print("Mi mascota se llama {} y tiene {} años.".format(nombre, edad))





# * 5. PARÁMETROS AVANZADOS: sep Y end
# ------------------------------------------
# ? Por defecto, print() separa los elementos con un espacio y hace un salto de línea al final.
# ? Podemos cambiar este comportamiento nativo usando 'sep' y 'end'.

# * Uso de 'sep' (Separator): Cambia el espacio automático por el texto que tú quieras.
print("Python", "es", "genial", sep="-")          # Muestra: Python-es-genial
print("Uno", "Dos", "Tres", sep=" | ")            # Muestra: Uno | Dos | Tres

# * Uso de 'end' (End of line): Cambia el salto de línea automático por otro carácter.
# ? Ideal para mantener impresiones consecutivas en la misma fila de la consola.
print("Cargando", end="... ")
print("¡Completado!")                             # Muestra: Cargando... ¡Completado! (en una sola línea)