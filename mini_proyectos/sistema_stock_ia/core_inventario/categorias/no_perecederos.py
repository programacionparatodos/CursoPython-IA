from core_inventario.producto_base import ProductoBase
from core_inventario.motor_ia import predecir_demanda_futura

class ProductoNoPerecedero(ProductoBase):
    def __init__(self, id_prod, nombre, stock_actual, historial_ventas, factor_estacional):
        super().__init__(id_prod, nombre, stock_actual, historial_ventas)
        self.factor_estacional = factor_estacional

    def convertir_a_diccionario(self):
        diccionario = super().convertir_a_diccionario()
        diccionario["tipo"] = "no_perecedero"
        diccionario["factor_estacional"] = self.factor_estacional
        return diccionario

    def evaluar_alerta_stock(self):
        prediccion_base = predecir_demanda_futura(self.obtener_historial())
        demanda_ajustada = prediccion_base * self.factor_estacional
        stock_seguridad_temporada = demanda_ajustada * 3

        if self.obtener_stock() <= stock_seguridad_temporada:
            print(f"Alerta IA Estacional: {self.nombre} requiere reposición. Stock actual: {self.obtener_stock()}. Demanda estacional proyectada: {demanda_ajustada:.1f}/día.")
            return

        print(f"No Perecedero {self.nombre} en óptimas condiciones para resistir la temporada actual.")