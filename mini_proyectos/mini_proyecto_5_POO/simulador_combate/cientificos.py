# mini_proyecto_5_POO/simulador_combate/cientificos.py

# ==============================================================================
# * [TEMA 11]: CLASE HIJA EXTENDIDA - CATEGORÍA CIENTÍFICOS TECNOLÓGICOS
# ==============================================================================

# * [TEMA 10]: Importamos la clase padre desde el archivo base del mismo paquete
from simulador_combate.base import PersonajeBase
import random

class CientificoTecnologico(PersonajeBase):
    def __init__(self, alias_entrada, salud_inicial, bateria_inicial=100, victorias_iniciales=0):
        # * [TEMA 11]: Enlazamos y reutilizamos el constructor de la clase padre
        super().__init__(alias_entrada, salud_inicial, victorias_iniciales)
        
        # * Atributos exclusivos de la especialización tecnológica
        self.bateria = bateria_inicial      # Tipo de dato: int (Porcentaje de energía)

    # ==========================================================================
    # ? ¿Qué hace?: Conecta el núcleo de energía para restablecer la batería al 100%.
    # ! Parámetros: Ninguno.
    # * Retorna: Nada (Modifica el estado de la variable de batería interna).
    # ==========================================================================
    def recargar_nucleo(self):
        self.bateria = 100
        print(f"🔋 [ENERGÍA]: {self.alias} reemplazó el núcleo de energía. ¡Batería al 100%!")

    # ==========================================================================
    # ? ¿Qué hace?: Ejecuta un ataque tecnológico aplicando POLIMORFISMO si tiene batería.
    # ! Parámetros: Ninguno.
    # * Retorna: Un número entero (int) con el daño infligido. Si no tiene batería, retorna 5.
    # ==========================================================================
    # * [TEMA 11]: POLIMORFISMO (Ataque de alta tecnología condicionado a la batería)
    def atacar(self):
        # * [TEMA 6]: CLÁUSULA DE GUARDA - Si la batería está agotada, usa un ataque de emergencia débil
        if self.bateria < 20:
            print(f"⚠️ [BATERÍA BAJA]: Los propulsores de {self.alias} están apagados. Ataque físico básico: 5 de daño.")
            return 5

        # * Camino Feliz: Consume energía y dispara un cañón repulsor o nanotecnología
        self.bateria = self.bateria - 20
        daño_tecnologico = random.randint(22, 38)
        print(f"🚀 [TECNOLOGÍA]: {self.alias} dispara sus cañones repulsores. Batería: {self.bateria}% | Daño: {daño_tecnologico}")
        return daño_tecnologico