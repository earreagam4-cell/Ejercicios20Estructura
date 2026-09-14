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