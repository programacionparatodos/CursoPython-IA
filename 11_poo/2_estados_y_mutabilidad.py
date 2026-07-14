# ==============================================================================
# # 11_poo -> 2_estados_y_mutabilidad.py
# ==============================================================================

# ==============================================================================
# * POO II: VARIABLES DE ESTADO, MUTABILIDAD Y PROTECCIÓN DE DATOS
# ==============================================================================

# ------------------------------------------------------------------------------
# * 2.1 Control del Estado y Protección Práctica de Atributos
# ------------------------------------------------------------------------------

class Vengador:
    def __init__(self, alias_entrada, salud_inicial):
        self.alias = alias_entrada        # Tipo de dato: str
        
        # * PROTECCIÓN DE DATOS: Usamos un guion bajo (_) al inicio del atributo.
        # * Esto le avisa a otros programadores: "¡Alerta! No alteres esta variable 
        # * directamente desde afuera haciendo trampas. Usa los métodos oficiales".
        self._salud = salud_inicial       # Tipo de dato: int
        self.escudo_activo = False        # Tipo de dato: bool (Estado inicial)

    # * Método oficial para leer la salud de forma segura (Equivalente a una función de lectura)
    def consultar_salud(self):
        return self._salud

    # * Métodos oficiales para alterar el estado interno de la salud de forma lógica
    def activar_defensa(self):
        self.escudo_activo = True
        print(f"🛡️ [{self.alias}]: Escudo de vibranium o campos de fuerza ACTIVADOS.")

    def recibir_daño(self, cantidad_impacto):
        if self.escudo_activo:
            print(f"🛡️ [{self.alias}]: ¡El escudo absorbió todo el impacto! Daño anulado.")
            self.escudo_activo = False # El escudo se agota tras el golpe
        else:
            self._salud = self._salud - cantidad_impacto
            print(f"💥 [{self.alias}]: ¡Impacto directo! Perdió {cantidad_impacto} de salud.")
            
            # Controlamos que la salud no baje de cero
            if self._salud < 0:
                self._salud = 0


# ------------------------------------------------------------------------------
# * 2.2 Mutabilidad en Acción (El cambio de estado)
# ------------------------------------------------------------------------------

print("--- 2.2 Viendo los cambios de Estado en la Consola ---")
capitan_america = Vengador("Capitán América", 100)

# * Estado Inicial
print(f"Estado Inicial -> Salud: {capitan_america.consultar_salud()} | Escudo: {capitan_america.escudo_activo}")

# * El Capitán recibe un ataque descuidado
capitan_america.recibir_daño(30)
print(f"Estado Post-Ataque -> Salud: {capitan_america.consultar_salud()}")

# * Activamos su defensa para el siguiente golpe
capitan_america.activar_defensa()
capitan_america.recibir_daño(40) # Este daño no le quitará salud

# * Estado Final
print(f"Estado Final -> Salud: {capitan_america.consultar_salud()} | Escudo: {capitan_america.escudo_activo}")


# ------------------------------------------------------------------------------
# * 2.3 Interacción entre Objetos (Pasar un objeto a otro objeto)
# ------------------------------------------------------------------------------

class DroideSoporte:
    def __init__(self, modelo_entrada):
        self.modelo = modelo_entrada

    # * Este método recibe un objeto completo de tipo 'Vengador' como argumento
    def curar_heroe(self, heroe_objetivo):
        salud_actual = heroe_objetivo.consultar_salud()
        
        print(f"\n🤖 [{self.modelo}]: Escaneando signos vitales de {heroe_objetivo.alias}...")
        
        if salud_actual < 100:
            # * El droide altera los datos internos del héroe usando su método oficial
            # * Simulamos la curación modificando internamente de forma controlada
            heroe_objetivo._salud = 100 
            print(f"🧪 [{self.modelo}]: Inyectando nanobots médicos... ¡{heroe_objetivo.alias} restaurado al 100%!")
        else:
            print(f"✅ [{self.modelo}]: {heroe_objetivo.alias} ya se encuentra en óptimas condiciones.")


print("\n--- 2.3 Cooperación Mutua entre Clases ---")
# * Creamos el droide asistente de Tony Stark
reparador_edith = DroideSoporte("E.D.I.T.H. Drone")

# * El droide interactúa directamente con el objeto del Capitán América
reparador_edith.curar_heroe(capitan_america)

# * Comprobamos que el estado del Capitán América cambió gracias al droide
print(f"Nueva salud del Capitán América: {capitan_america.consultar_salud()}%")


# ------------------------------------------------------------------------------
# 🚀 REFUERZO POST-CLASE: Ejemplos Extra para Practicar en Casa (Clase 2 - POO)
# ------------------------------------------------------------------------------

# * Ejemplo A: Controlar Estados mediante Diccionarios de Estados Fijos
# ? Podemos usar un diccionario como mapa de estados permitidos para asegurar
# ? que un objeto solo cambie a estados válidos en su ciclo de vida.
# class TrajeIronMan:
#     def __init__(self):
#         self.estados_validos = {0: "Apagado", 1: "Modo Vuelo", 2: "Modo Combate"}
#         self.estado_actual = self.estados_validos[0]
#
#     def cambiar_modo(self, codigo_int):
#         if codigo_int in self.estados_validos:
#             self.estado_actual = self.estados_validos[codigo_int]
#             print(f"🤖 [SISTEMA] Sistema cambiado con éxito a: {self.estado_actual}")
#
# print("\n--- Refuerzo A: Diccionario de Control de Estados ---")
# mark_85 = TrajeIronMan()
# mark_85.cambiar_modo(2)


# * Ejemplo B: Historial de Cambios de Estado usando Listas (Efecto Bitácora)
# ? Cada vez que un atributo del objeto muta o cambia, podemos registrar esa
# ? acción en una lista interna para tener un registro histórico del personaje.
# class RegistroMisiones:
#     def __init__(self, alias):
#         self.alias = alias
#         self.bitacora = [] # list de str vacía para el historial
#
#     def registrar_evento(self, descripcion_evento):
#         self.bitacora.append(descripcion_evento)
#
# print("\n--- Refuerzo B: Bitácora de Estados usando Listas ---")
# espia_natasha = RegistroMisiones("Black Widow")
# espia_natasha.registrar_evento("Infiltración en base de Hydra exitosa.")
# espia_natasha.registrar_evento("Rescate de rehenes completado.")
# print(f"Historial de {espia_natasha.alias}: {espia_natasha.bitacora}")


# * Ejemplo C: Mutabilidad Masiva en Conjuntos (Sets de Objetos)
# ? Si guardamos múltiples objetos dentro de un set (conjunto), podemos recorrerlos
# ? y alterar el estado de todos ellos en bloque usando un solo bucle 'for'.
# # Código teórico de ejemplo interactuando con instancias previas:
# # grupo_heroes_set = {capitan_america, heroe_uno}
# # for heroe in grupo_heroes_set:
# #     heroe.recibir_daño(10)
# print("\n--- Refuerzo C: Mutabilidad Masiva en Colecciones ---")
# print("Se puede alterar el estado de múltiples objetos iterando sobre un set.")


# * Ejemplo D: Almacenar un Objeto Completo dentro de una Llave de Diccionario
# ? Los diccionarios pueden guardar un objeto completo dentro de sus valores. Esto
# ? es muy útil para buscar héroes por su código único de identificación.
# class FichaIdentidad:
#     def __init__(self, nombre_real):
#         self.nombre_real = nombre_real
#
# print("\n--- Refuerzo D: Objetos Guardados en Diccionarios ---")
# base_datos_shield = {}
# ficha_thor = FichaIdentidad("Thor Odinson")
# # * Guardamos el objeto completo usando un código string como clave
# base_datos_shield["AVN-003"] = ficha_thor
# print(f"Búsqueda exitosa en S.H.I.E.L.D.: {base_datos_shield['AVN-003'].nombre_real}")