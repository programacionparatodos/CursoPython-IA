from core_inventario.producto_base import ProductoBase
from core_inventario.motor_ia import predecir_demanda_futura

class ProductoPerecedero(ProductoBase):
    def __init__(self, id_prod, nombre, stock_actual, historial_ventas, dias_caducidad):
        super().__init__(id_prod, nombre, stock_actual, historial_ventas)
        self.dias_caducidad = dias_caducidad

    def convertir_a_diccionario(self):
        diccionario = super().convertir_a_diccionario()
        diccionario["tipo"] = "perecedero"
        diccionario["dias_caducidad"] = self.dias_caducidad
        return diccionario

    def evaluar_alerta_stock(self):
        prediccion = predecir_demanda_futura(self.obtener_historial())
        stock_seguridad = prediccion * 2

        if self.dias_caducidad <= 3:
            print(f"ALERTA CRÍTICA: {self.nombre} (ID: {self.id_prod}) vence en {self.dias_caducidad} días. ¡Liquidar stock!")
            return

        if self.obtener_stock() <= stock_seguridad:
            print(f"Alerta IA: Stock bajo para el perecedero {self.nombre}. Stock actual: {self.obtener_stock()}. Sugerencia: Reponer urgente.")
            return

        print(f"Perecedero {self.nombre} estable. El stock actual cubre la demanda estimada por la IA.")