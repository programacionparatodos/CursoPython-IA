# * Base de datos interna usando un Diccionario con Listas adentro
inventario_canino = {
    "zona": "Pabellón A",
    "capacidad_maxima": 10, 
    "pacientes_actuales": ["Lulú", "Cobby", "Chiqui"] # lista de strings
}

def registrar_perro(nombre, edad, peso, esta_vacunado):
    # * Recibe datos simples y los empaqueta en un diccionario estructurado
    perro_nuevo = {
        "nombre": nombre,           # str
        "edad": edad,               # int
        "peso": peso,               # float
        "vacunado": esta_vacunado   # bool
    }
    
    # * Agregamos al perrito a la lista del inventario de la zona
    inventario_canino["pacientes_actuales"].append(nombre)
    
    print(f"🐶 [PERROS] {nombre} ha sido ingresado con éxito a la {inventario_canino['zona']}.")
    return perro_nuevo # Devolvemos el diccionario con todos sus tipos de datos mezclados