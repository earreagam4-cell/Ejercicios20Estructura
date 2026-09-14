#Inversor de secuencias

class InversorSecuencia:
    def __init__(self):
        self.invertidos = []
    def invertir_lista(self, lista):
        invertida = lista[::-1]
        self.invertidos.append(invertida)
        return invertida
    def invertir_multiples(self, *args):
        resultado = {}
        for lista in args:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida 
        return resultado

invertido = InversorSecuencia()
print(invertido.invertir_lista([1, 2, 3, 4, 5]))
print(invertido.invertir_multiples([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))