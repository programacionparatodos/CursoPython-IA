# mini_proyecto_5_POO/simulador_combate/hechiceros.py

# ==============================================================================
# * [TEMA 11]: CLASE HIJA EXTENDIDA - CATEGORÍA HECHICEROS MÍSTICOS
# ==============================================================================

# * [TEMA 10]: Importamos la clase padre desde el archivo base del mismo paquete
from simulador_combate.base import PersonajeBase
import random

class HechiceroMistico(PersonajeBase):
    def __init__(self, alias_entrada, salud_inicial, mana_inicial, victorias_iniciales=0):
        # * [TEMA 11]: Enlazamos y reutilizamos el constructor de la clase padre
        super().__init__(alias_entrada, salud_inicial, victorias_iniciales)
        
        # * Atributos exclusivos de la especialización de hechiceros
        self.mana = mana_inicial            # Tipo de dato: int (Energía mística)

    # ==========================================================================
    # ? ¿Qué hace?: Incrementa los puntos de energía mística interna del hechicero.
    # ! Parámetros: Ninguno.
    # * Retorna: Nada (Modifica el estado de la variable de maná interna).
    # ==========================================================================
    def meditar(self):
        self.mana = self.mana + 35
        # * [TEMA 6]: Controlamos que el maná no supere un límite lógico de 100
        if self.mana > 100:
            self.mana = 100
        print(f"🔮 [MANÁ]: {self.alias} canalizó artes ancestrales. Recuperó maná. (Actual: {self.mana} MP)")

    # ==========================================================================
    # ? ¿Qué hace?: Ejecuta un ataque mágico aplicando POLIMORFISMO si tiene maná.
    # ! Parámetros: Ninguno.
    # * Retorna: Un número entero (int) con el daño infligido. Si no tiene maná, retorna 0.
    # ==========================================================================
    # * [TEMA 11]: POLIMORFISMO (Estructura de ataque personalizada basada en maná)
    def atacar(self):
        # * [TEMA 6]: CLÁUSULA DE GUARDA - Si no tiene suficiente energía mística, el ataque falla
        if self.mana < 25:
            print(f"❌ [FALLO]: {self.alias} intentó conjurar, ¡pero no tiene suficiente maná! Debe meditar.")
            return 0 # Daño nulo debido a la falta de recurso mágico

        # * Camino Feliz: Gasta maná y genera un impacto destructivo aleatorio
        self.mana = self.mana - 25
        daño_mistico = random.randint(25, 40)
        print(f"✨ [HECHIZO]: {self.alias} lanza Rayos Místicos gastando 25 de maná e infligiendo {daño_mistico} de daño.")
        return daño_mistico