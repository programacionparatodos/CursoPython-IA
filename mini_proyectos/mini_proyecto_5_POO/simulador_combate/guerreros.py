# mini_proyecto_5_POO/simulador_combate/guerreros.py

# ==============================================================================
# * [TEMA 11]: CLASE HIJA EXTENDIDA - CATEGORÍA GUERREROS FÍSICOS
# ==============================================================================

# * [TEMA 10]: Importamos la clase padre desde el archivo base del mismo paquete
from simulador_combate.base import PersonajeBase
import random

class GuerreroFisico(PersonajeBase):
    def __init__(self, alias_entrada, salud_inicial, arma_entrada, victorias_iniciales=0):
        # * [TEMA 11]: Enlazamos y reutilizamos el constructor de la clase padre
        super().__init__(alias_entrada, salud_inicial, victorias_iniciales)
        
        # * Atributos exclusivos de la especialización de guerreros
        self.arma = arma_entrada            # Tipo de dato: str
        self.escudo_vibranium = False       # Tipo de dato: bool (Inicia desactivado)

    # ==========================================================================
    # ? ¿Qué hace?: Activa el estado de defensa absoluta del guerrero.
    # ! Parámetros: Ninguno (Usa las variables internas a través de self).
    # * Retorna: Nada (Solo imprime el cambio de estado en la consola).
    # ==========================================================================
    def activar_defensa(self):
        self.escudo_vibranium = True
        print(f"🛡️ [DEFENSA]: ¡{self.alias} activó su escudo y el impacto fue anulado.")

    # ==========================================================================
    # ? ¿Qué hace?: Calcula el daño físico infligido al enemigo usando fuerza bruta.
    # ! Parámetros: Ninguno.
    # * Retorna: Un número entero (int) con el valor del impacto aleatorio.
    # ==========================================================================
    def atacar(self):
        # * [TEMA 5 / TEMA 10]: Calculamos un golpe aleatorio basado en el azar
        daño_base = random.randint(20, 35)
        print(f"⚔️ [ATAQUE]: {self.alias} arremete con su {self.arma} infligiendo {daño_base} de daño físico.")
        return daño_base

    # ==========================================================================
    # ? ¿Qué hace?: Procesa el impacto recibido aplicando POLIMORFISMO.
    # ! Parámetros: daño_recibido (int) -> Cantidad de daño que intenta infligir el rival.
    # * Retorna: Nada (Modifica el estado interno de salud o rompe el escudo).
    # ==========================================================================
    # * [TEMA 11]: POLIMORFISMO (Sobrescribimos el método del padre para el escudo)
    def recibir_impacto(self, daño_recibido):
        # * [TEMA 6]: CLÁUSULA DE GUARDA - Si el escudo está activo, bloqueamos el daño de inmediato
        if self.escudo_vibranium:
            print(f"🛡️ [BLOQUEO]: El escudo de vibranium absorbió el golpe. ¡0 daño recibido por {self.alias}!")
            self.escudo_vibranium = False # El escudo se agota tras el impacto protector
            return # Cortamos el método aquí evitando que la salud disminuya

        # * Camino Feliz: Si no tenía el escudo levantado, delegamos la resta normal a la clase padre
        super().recibir_impacto(daño_recibido)