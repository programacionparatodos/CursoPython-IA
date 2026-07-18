class ProductoBase:
    def __init__(self, id_prod, nombre, stock_actual, historial_ventas):
        self.id_prod = id_prod
        self.nombre = nombre

        self._stock_actual = stock_actual
        self._historial_ventas = historial_ventas

    def obtener_stock(self):
        return self._stock_actual
    
    def obtener_historial(self):
        return self.historial_ventas
    
    def registrar_venta_diaria(self, cantidad):
        if cantidad > self._stock_actual:
            print("Error: No puedes vender más de lo que tienes en stock")
            return
        
        self._stock_actual -= cantidad
        self._historial_ventas.append(cantidad)

        if len(self._historial_ventas) > 5:
            self._historial_ventas.pop(0)

    def convertir_a_diccionario(self):
        return {
            "id_prod": self.id_prod,
            "nombre": self.nombre,
            "stock_actual": self._stock_actual,
            "historial_ventas": self._historial_ventas,
            "tipo": "base"
        }
    
    def evaluar_alerta_stock(self):
        pass