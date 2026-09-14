#Inventario de productos

class Inventario:
    def __init__(self):
        self.stock = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if self.stock[producto] - cantidad >= 0:
            self.stock[producto] -= cantidad
            return True
        return False
    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]

inventario = Inventario()
inventario.agregar_stock("camiseta", 10)
inventario.agregar_stock("zapatilla", 20)
inventario.agregar_stock("bola", 30)        
inventario.agregar_stock("zapatilla", 40)
print(inventario.productos_bajo_stock(20))
print(inventario.restar_stock("camiseta", 5))
print(inventario.productos_bajo_stock(20))