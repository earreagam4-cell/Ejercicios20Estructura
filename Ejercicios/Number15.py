#Divisores de un número

class DivisorFinder:
    def __init__(self):
        self.divisores = []
    def encontrar_divisores(self, numero):
        self.divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                self.divisores.append(i)
        return self.divisores
    def es_perfecto(self, numero):
        return sum(self.divisores) - numero == 0
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

encontrador = DivisorFinder()
print(encontrador.encontrar_divisores(10))
print(encontrador.es_perfecto(10))     

# Hecho por mi 

class Numeros:

    def __init__(self):
        self.divisores = {}

    def encontrar(self, numero):
        resultado = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                resultado.append(i)

        return tuple(resultado)

    def es_perfecto(self, numero):
        divisores = self.encontrar(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        return suma == numero


n = Numeros()

print(n.encontrar(6))
print(n.es_perfecto(6))
