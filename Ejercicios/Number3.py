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
#Hecho por mi 
class Libros:

    def __init__(self):
        self.libros = {}

    def agregar(self, nombre, precio):
        self.libros[nombre] = precio

    def total(self):
        total = 0

        for precio in self.libros.values():
            total += precio

        return total

    def buscar(self, minimo, maximo):
        resultado = []

        for nombre, precio in self.libros.items():
            if minimo <= precio <= maximo:
                resultado.append(nombre)

        return resultado


l = Libros()

l.agregar("La culpa es de la vaca", 10)
l.agregar("Abitos Atomicos", 15)
l.agregar("Mujercitas", 8)

print(l.libros)
print(l.total())
print(l.buscar(8, 10))
