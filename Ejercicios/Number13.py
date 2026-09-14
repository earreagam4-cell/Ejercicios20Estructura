#Combinador de listas

class CombinadorListas:
    def __init__(self):
        self.listas = []
    def intercalar(self, lista1, lista2):
        return lista1 + lista2[::-1]
    def intercalar_multiples(self, *args):
        resultado = []
        for lista in args:
            resultado.append(self.intercalar(lista, lista))
        return resultado
combinador = CombinadorListas()
print(combinador.intercalar([1, 2, 3], [4, 5, 6]))
print(combinador.intercalar_multiples([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])) 
