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

# Hecho por mi 

class Almacen:

    def __init__(self):
        self.productos = {}

    def agregar(self, producto, cantidad):
        self.productos[producto] = cantidad

    def retirar(self, producto, cantidad):

        if producto in self.productos:

            if self.productos[producto] >= cantidad:
                self.productos[producto] -= cantidad
                return True

        return False

    def pocos(self, minimo):

        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado


a = Almacen()

a.agregar("Bread", 20)
a.agregar("Sugar", 5)

print(a.productos)

print(a.retirar("Bread", 10))

print(a.productos)

print(a.pocos(15))
