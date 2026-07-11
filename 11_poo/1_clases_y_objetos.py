# ==============================================================================
# # 11_poo -> 1_clases_y_objetos.py
# ==============================================================================

# ==============================================================================
# * POO I: EL MOLDE (CLASE) Y EL HÉROE REAL (OBJETO O INSTANCIA)
# ==============================================================================

class Heroe:
    # * El constructor '__init__' es el encargado de dar vida al personaje.
    # * 'self' representa al héroe específico que se está creando en ese instante.
    def __init__(self, nombre_entrada, alias_entrada, energia_entrada):
        # * Atributos: Son las características internas del superhéroe
        self.nombre = nombre_entrada      # Tipo de dato: str
        self.alias = alias_entrada        # Tipo de dato: str
        self.energia = energia_entrada    # Tipo de dato: int (0 a 100)
        self.traje_puesto = False         # Tipo de dato: bool (Nacen en ropa civil)

    # * Métodos: Son las acciones o superpoderes que el héroe sabe ejecutar
    def equipar_armadura(self):
        if not self.traje_puesto:
            self.traje_puesto = True
            print(f"🦾 [{self.alias}]: ¡Traje de combate desplegado al 100%!")
        else:
            print(f"⚠️ [{self.alias}]: El traje ya está equipado en el cuerpo.")

    def lanzar_ataque(self):
        # * Gracias a 'self', el método sabe exactamente quién ataca sin pasarle parámetros
        if self.traje_puesto:
            print(f"💥 [{self.alias}]: Ejecutando ataque principal contra el enemigo.")
            self.energia = self.energia - 10 # El ataque consume energía interna
        else:
            print(f"❌ [{self.alias}]: ¡No puedes atacar! Primero debes ponerte el traje.")


# ------------------------------------------------------------------------------
# * 1.2 Fabricando Superhéroes en la Vida Real (Instanciación)
# ------------------------------------------------------------------------------

print("--- 1.2 Creando Héroes Reales en la Memoria de Python ---")

# * Usamos el molde 'Heroe' para crear dos personajes independientes
heroe_uno = Heroe("Tony Stark", "Iron Man", 100)
heroe_dos = Heroe("Peter Parker", "Spider-Man", 90)

# * Accedemos a sus características (Atributos) usando la sintaxis del punto (.)
print(f"Identidad secreta: {heroe_uno.nombre} | Nombre de héroe: {heroe_uno.alias}")
print(f"Identidad secreta: {heroe_dos.nombre} | Nombre de héroe: {heroe_dos.alias}")


# ------------------------------------------------------------------------------
# * 1.3 Activando los Superpoderes (Invocación de Métodos)
# ------------------------------------------------------------------------------

print("\n--- 1.3 Probando las Acciones de los Objetos ---")

# * Intentamos atacar con Iron Man sin su armadura
heroe_uno.lanzar_ataque()

# * Ahora equipamos el traje y volvemos a intentar el ataque
heroe_uno.equipar_armadura()
heroe_uno.lanzar_ataque()

# * Revisamos el estado de su energía para ver cómo disminuyó de forma interna
print(f"⚡ Energía restante de {heroe_uno.alias}: {heroe_uno.energia}%")

# ! NOTA DE OBSERVACIÓN: Mira cómo 'heroe_dos' (Spider-Man) no se ve afectado. 
# ! Su energía sigue intacta en {heroe_dos.energia}% y su traje sigue guardado 
# ! porque cada objeto en memoria es completamente independiente.


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa (Clase 1 - POO)
# ------------------------------------------------------------------------------

# * Ejemplo A: Lectura de Constantes de Héroes (Uso de Tuplas en Atributos)
# ? Los objetos pueden almacenar tuplas inmutables como parte de sus atributos fijos,
# ? asegurando que las coordenadas de su base de operaciones nunca se alteren por error.
# class BaseSecreta:
#     def __init__(self, nombre, coordenadas_tuple):
#         self.nombre = nombre
#         self.ubicacion = coordenadas_tuple # tuple de floats (Latitud, Longitud)
#
# print("\n--- Refuerzo A: Datos Inmutables en Atributos ---")
# torre_avengers = BaseSecreta("Torre Stark", (40.7527, -73.9772))
# print(f"Ubicación de la {torre_avengers.nombre}: {torre_avengers.ubicacion}")


# * Ejemplo B: Evitar Poderes Duplicados en el Perfil (Uso de Sets)
# ? Podemos usar conjuntos (sets) dentro de un método para asegurarnos de que si 
# ? un héroe intenta registrar un superpoder repetido, Python lo filtre automáticamente.
# class RegistroPoderes:
#     def __init__(self, alias):
#         self.alias = alias
#         self.lista_poderes = ["Volar", "Fuerza"] # list inicial
#
#     def añadir_poderes_unicos(self, nuevos_poderes_list):
#         # * Fusionamos listas y removemos duplicados usando un conjunto (set)
#         lista_combinada = self.lista_poderes + nuevos_poderes_list
#         self.lista_poderes = list(set(lista_combinada))
#
# print("\n--- Refuerzo B: Filtrado de Datos con Sets en Clases ---")
# ironman_poderes = RegistroPoderes("Iron Man")
# ironman_poderes.añadir_poderes_unicos(["Rayos Láser", "Volar", "Inteligencia"])
# print(f"Poderes finales de {ironman_poderes.alias}: {ironman_poderes.lista_poderes}")


# * Ejemplo C: Objetos Almacenados en Colecciones Nativas (Listas de Objetos)
# ? Una lista común de Python puede almacenar múltiples objetos completos creados 
# ? desde una clase, permitiéndonos iterar sobre ellos de forma masiva con un 'for'.
# class Escuadrón:
#     def __init__(self, nombre_bando):
#         self.bando = nombre_bando
#         self.miembros = [] # Lista que guardará objetos reales adentro
#
# print("\n--- Refuerzo C: Almacenamiento de Objetos en Listas ---")
# equipo_cap = Escuadrón("Team Cap")
# # * Inyectamos directamente las instancias creadas en el archivo principal
# equipo_cap.miembros.append(heroe_dos) # Agrega el objeto completo de Spider-Man
# print(f"Miembros en el {equipo_cap.bando}: {len(equipo_cap.miembros)} héroe reclutado.")


# * Ejemplo D: Conversión de Objetos a Diccionarios en Tiempo Real
# ? Un método puede recolectar todos los atributos individuales del objeto y 
# ? empaquetarlos en un diccionario clásico para facilitar el envío de datos a redes.
# class ConvertidorFicha:
#     def __init__(self, alias, bando, nivel):
#         self.alias = alias
#         self.bando = bando
#         self.nivel = nivel
#
#     def exportar_a_diccionario(self):
#         # * Retorna una estructura limpia de tipo diccionario (dict)
#         return {"alias": self.alias, "bando": self.bando, "poder_rango": self.nivel}
#
# print("\n--- Refuerzo D: Exportación de Objetos a Diccionarios ---")
# ficha_antman = ConvertidorFicha("Ant-Man", "Avengers", 75)
# dict_generado = ficha_antman.exportar_a_diccionario()
# print(f"Estructura dict creada para el servidor: {dict_generado}")