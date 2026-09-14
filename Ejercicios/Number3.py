#generador de números totales

class CarroCompras:
    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        return sum(self.articulos.values())
    def articulos_por_rango(self, precio_min, precio_max):
        return [articulo for articulo in self.articulos.items() if precio_min <= articulo[1] <= precio_max]

carro = CarroCompras()
carro.agregar_articulo("camiseta", 10)
carro.agregar_articulo("zapatilla", 20)
carro.agregar_articulo("bola", 30)
carro.agregar_articulo("zapatilla", 40)
print(carro.total_carrito())
print(carro.articulos_por_rango(20, 30))    