# ==============================================================================
# # 11_poo -> 3_herencia_y_polimorfismo.py
# ==============================================================================

# ==============================================================================
# * POO III: HERENCIA Y REUTILIZACIÓN DE ESTRUCTURAS (`SUPER`)
# ==============================================================================

# ------------------------------------------------------------------------------
# * 3.1 Creación de la Clase Base o Clase Padre
# ------------------------------------------------------------------------------

class ReclutaSHIELD:
    def __init__(self, nombre_real, rango_str):
        # * Atributos que TODOS los agentes e integrantes poseen por igual
        self.nombre = nombre_real
        self.rango = rango_str
        self.en_mision = False # Estado inicial estándar

    def reportar_estado(self):
        print(f"📋 [S.H.I.E.L.D.] Agente {self.nombre} en rango {self.rango}. ¿En misión?: {self.en_mision}")


# ------------------------------------------------------------------------------
# * 3.2 Clases Hijas Extendidas mediante la función `super()`
# ------------------------------------------------------------------------------

# * Clase Hija 1: Guerrero de Combate Cuerpo a Cuerpo
class GuerreroCuerpoACuerpo(ReclutaSHIELD):
    def __init__(self, nombre_real, rango_str, arma_str):
        # * Activamos el constructor del padre para reutilizar nombre y rango
        super().__init__(nombre_real, rango_str)
        # * Atributo exclusivo de la clase hija
        self.arma_principal = arma_str # Tipo de dato: str

    def ejecutar_combate(self):
        self.en_mision = True
        print(f"⚔️ [{self.nombre}]: Atacando en primera línea usando: {self.arma_principal}.")


# * Clase Hija 2: Mago o Especialista Místico
class HechiceroMistico(ReclutaSHIELD):
    def __init__(self, nombre_real, rango_str, puntos_mana_int):
        super().__init__(nombre_real, rango_str)
        # * Atributo exclusivo del hechicero
        self.mana = puntos_mana_int # Tipo de dato: int

    def lanzar_hechizo(self, costo_energia):
        if self.mana >= costo_energia:
            self.mana = self.mana - costo_energia
            self.en_mision = True
            print(f"🔮 [{self.nombre}]: Conjurando defensas místicas. Maná restante: {self.mana}")
        else:
            print(f"❌ [{self.nombre}]: ¡Sin energía mística suficiente para el conjuro!")


# ------------------------------------------------------------------------------
# * 3.3 El Concepto de Polimorfismo (Sobrescritura de Métodos)
# ------------------------------------------------------------------------------

class EspiaInfiltrado(ReclutaSHIELD):
    def __init__(self, nombre_real, rango_str):
        super().__init__(nombre_real, rango_str)

    # * SOBRESCRITURA: Reescribimos el método del padre para cambiar el mensaje
    def reportar_estado(self):
        # Un espía no puede revelar sus datos de forma estándar
        print(f"🥷 [SISTEMA ALTERADO] Agente encubierto. Ubicación e identidad CLASIFICADAS.")


# ------------------------------------------------------------------------------
# * 3.4 Desplegando el Escuadrón Heredado en Consola
# ------------------------------------------------------------------------------

print("--- 3.4 Demostración de Herencia y Polimorfismo ---")

# * Instanciamos las clases hijas pasándole sus datos correspondientes
heroe_guerrero = GuerreroCuerpoACuerpo("Thor", "Dios del Trueno", "Mjolnir")
heroe_mago = HechiceroMistico("Stephen Strange", "Hechicero Supremo", 80)
heroe_espia = EspiaInfiltrado("Natasha Romanoff", "Nivel 7")

# * 1. Probamos atributos heredados y métodos propios
print(f"El arma de {heroe_guerrero.nombre} es el {heroe_guerrero.arma_principal}.")
heroe_guerrero.ejecutar_combate()

# * 2. Probamos la lógica propia de la otra clase hija
heroe_mago.lanzar_hechizo(30)

# * 3. Probamos el Polimorfismo (El método alterado del espía)
print("\n--- Comparativa de Métodos Comunes vs Sobrescriptos ---")
heroe_guerrero.reportar_estado() # Muestra el formato estándar del padre
heroe_espia.reportar_estado()    # Muestra el formato modificado del hijo


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa (Clase 3 - POO)
# ------------------------------------------------------------------------------

# * Ejemplo A: Almacenar Clases Hijas en un Diccionario por Categorías
# ? Podemos usar las clases hijas como valores dentro de un diccionario para 
# ? clasificar dinámicamente qué tipo de héroe queremos instanciar según la clave.
# class Tanque(ReclutaSHIELD):
#     def __init__(self, nombre, rango):
#         super().__init__(nombre, rango)
#         self.resistencia = 500
#
# print("\n--- Refuerzo A: Mapeo de Clases Hijas en Diccionarios ---")
# catálogo_clases = {"tanque": Tanque}
# # * Instanciamos llamando directamente a la clave del diccionario
# heroe_hulk = catálogo_clases["tanque"]("Bruce Banner", "Fuerza Bruta")
# print(f"Héroe creado dinámicamente: {heroe_hulk.nombre} con {heroe_hulk.resistencia} de aguante.")


# * Ejemplo B: Validar el Tipo de Objeto con `isinstance` y Tuplas de Clases
# ? Python nos permite evaluar si un objeto pertenece a una clase específica o a
# ? un grupo de clases permitidas usando una tupla en la función 'isinstance'.
# print("\n--- Refuerzo B: Verificación de Parentesco con isinstance ---")
# # * Preguntamos si 'heroe_guerrero' (creado en el archivo base) es un recluta de SHIELD
# es_agente = isinstance(heroe_guerrero, ReclutaSHIELD)
# # * Preguntamos si pertenece a un conjunto de clases específicas (usando una tupla)
# es_especialista = isinstance(heroe_mago, (HechiceroMistico, EspiaInfiltrado))
# print(f"¿Thor es heredero de SHIELD?: {es_agente}")
# print(f"¿Strange pertenece al grupo místico/espía?: {es_especialista}")


# * Ejemplo C: Ejecución Polimórfica Masiva usando Listas (El bucle unificado)
# ? El polimorfismo brilla cuando metes diferentes objetos hijos en una misma lista 
# ? e invocas el mismo método heredado; cada uno responderá a su manera única.
# # Código teórico de ejemplo interactuando con instancias previas:
# # lista_batallon = [heroe_guerrero, heroe_espia]
# # for combatiente in lista_batallon:
# #     combatiente.reportar_estado() # Cada uno ejecuta su propia versión del método
# print("\n--- Refuerzo C: Bucle Polimórfico con Listas ---")
# print("Una lista puede unificar distintos hijos y hacerlos reportarse a su modo.")


# * Ejemplo D: Filtrar Atributos Exclusivos usando Conjuntos (Sets) de Propiedades
# ? Podemos usar conjuntos (sets) para comparar las propiedades internas de una clase 
# ? hija frente a la clase padre y descubrir rápidamente qué variables se añadieron.
# print("\n--- Refuerzo D: Comparación de Atributos con Sets ---")
# # * Extraemos las variables internas de los moldes usando __dict__ y las pasamos a sets
# atributos_padre = set(ReclutaSHIELD("Test", "Rango").__dict__.keys())
# atributos_hijo = set(GuerreroCuerpoACuerpo("Test", "Rango", "Espada").__dict__.keys())
# # * Restamos conjuntos para encontrar la diferencia o exclusividad
# exclusivo_hijo = atributos_hijo - atributos_padre
# print(f"Atributos agregados exclusivamente en la clase Hija: {exclusivo_hijo}")