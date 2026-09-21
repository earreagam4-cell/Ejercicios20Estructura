#Detector de números pares e impares

class AnalizadorNumeros:
    def __init__(self):
        self.numeros = []
    def es_par(self, numero):
        return numero % 2 == 0
    def separar(self, *args):
        resultado = {'pares': [], 'impares': []}
        for numero in args:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)
        return resultado
    def cantidad_pares_impares(self):
        return len(self.numeros['pares']), len(self.numeros['impares'])
analizador = AnalizadorNumeros()
analizador.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(analizador.separar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(analizador.cantidad_pares_impares())  
#Hecho por mi 

class Analizador:

    def __init__(self):
        self.numeros = []

    def es_positivo(self, numero):
        return numero >= 0

    def separar(self, *numeros):
        resultado = {
            "positivos": [],
            "negativos": []
        }

        for numero in numeros:
            self.numeros.append(numero)

            if self.es_positivo(numero):
                resultado["positivos"].append(numero)
            else:
                resultado["negativos"].append(numero)

        return resultado


a = Analizador()

print(a.separar(5, -2, 8, -1, 3))
