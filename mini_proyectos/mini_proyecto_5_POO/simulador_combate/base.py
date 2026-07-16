# mini_proyecto_5_POO/simulador_combate/base.py

# ==============================================================================
# * [TEMA 11]: CLASE BASE O PADRE - INFRAESTRUCTURA GENERAL DE HÉROES
# ==============================================================================

class PersonajeBase:
    def __init__(self, alias_entrada, salud_inicial, victorias_iniciales=0):
        # * [TEMA 3 / TEMA 11]: ATRIBUTOS PÚBLICOS DE IDENTIFICACIÓN Y ESTADO
        self.alias = alias_entrada              # Tipo de dato: str
        self.victorias = victorias_iniciales    # Tipo de dato: int (Cargado desde JSON o 0)
        self.esta_vivo = True                   # Tipo de dato: bool

        # * [TEMA 11]: ENCAPSULAMIENTO PRÁCTICO (BLINDAJE DE ATRIBUTOS SENSIBLES)
        # ? Colocamos un guion bajo (_) para avisarle al sistema que la salud no se 
        # ? debe alterar directamente desde fuera con asignaciones como heroe.salud = 999
        self._salud = salud_inicial             # Tipo de dato: int (Rango de 0 a 100)

    # ==========================================================================
    # ? ¿Qué hace?: Devuelve de forma segura el valor actual de la salud protegida.
    # ! Parámetros: Ninguno (Usa las variables internas a través de self).
    # * Retorna: Un número entero (int) con el porcentaje de vida restante.
    # ==========================================================================
    def consultar_salud(self):
        return self._salud

    # ==========================================================================
    # ? ¿Qué hace?: Resta la salud de forma lógica y evalúa si el héroe cae debilitado.
    # ! Parámetros: daño_recibido (int) -> Cantidad de impacto aritmético a aplicar.
    # * Retorna: Nada (Modifica el estado interno de las variables del objeto).
    # ==========================================================================
    # * [TEMA 6 / TEMA 11]: MÉTODO MUTADOR CONTROLADO
    def recibir_impacto(self, daño_recibido):
        # * [TEMA 5]: Operador aritmético de resta secuencial
        self._salud = self._salud - daño_recibido

        # * [TEMA 6]: Estructura condicional para evitar números negativos en salud
        if self._salud <= 0:
            self._salud = 0
            self.esta_vivo = False
            print(f"💀 [ARENA]: ¡{self.alias} ha caído derrotado en combate!")
        else:
            print(f"💥 [ARENA]: {self.alias} recibió {daño_recibido} de daño. (Salud restante: {self._salud}%)")