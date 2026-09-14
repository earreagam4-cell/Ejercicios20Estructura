#Selector de rango con tuplas

class SelectorRango:
    def __init__(self):
        self.rangos = []
    def crear_rango(self, inicio, fin):
        return (inicio, fin)
    def elementos_en_multiples_rangos(self, *args):
        resultado = []
        for rango in args:
            resultado.extend(self.crear_rango(inicio, fin) for inicio, fin in rango)
        return list(set(resultado))

selector = SelectorRango()
print(selector.elementos_en_multiples_rangos((1, 10), (2, 5), (3, 8), (4, 9), (5, 12), (6, 15), (7, 18), (8, 20), (9, 25), (10, 30)))       
