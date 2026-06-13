# Una variable es una caja que almacena un valor

# * REGLAS PARA NOMBRAR VARIABLES
# * Solo pueden contener: Letras mayúsculas, minúsculas, dítigos, _
# * Deben empezar con una letra o _ (nunca con un dígito)
# * No pueden ser palabras reservadas

# * Asignación simple (Individual)
edad = 25
nombre = 'Rene'

# * Asignación múltiple (Al mismo tiempo)
a, b, c = 10, 20, 30

# * El mismo valor para múltiples variables
a = b = c = 0

# * Asignar el valor de una variable a otra variable
precio_original = 100
precio_final = precio_original # precio_final ahora vale 100

# ! Importante: si cambiamos el valor de precio_original no cambia el valor
# ! del precio_final
precio_original = 150
print(precio_final)
