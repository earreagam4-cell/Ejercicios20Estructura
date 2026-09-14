#Matriz de distancias

class CalculadorDistancia:
    def __init__(self):
        self.lista = []
    def distancia_euclidiana(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    def punto_mas_cercano(self, referencia, *puntos):
        distancias = [self.distancia_euclidiana(referencia, punto) for punto in puntos]
        return puntos[distancias.index(min(distancias))]

calculador = CalculadorDistancia()
print(calculador.punto_mas_cercano((0, 0), (1, 1), (2, 2), (3, 3), (4, 4)))     