#Estadísticas de temperatura

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)
    def registrar_multiples(self, *args):
        for temperatura in args:
            self.registrar_temperatura(temperatura)
    def minima(self):
        return min(self.temperaturas)
    def maxima(self):
        return max(self.temperaturas)
    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

gestor = GestorTemperatura()
gestor.registrar_multiples(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(gestor.minima())
print(gestor.maxima())
print(gestor.promedio())    

#Hecho por mi 

class Calificaciones:

    def __init__(self):
        self.calificaciones = []

    def agregar(self, *notas):
        for nota in notas:
            self.calificaciones.append(nota)

    def mayor(self):
        return max(self.calificaciones)

    def menor(self):
        return min(self.calificaciones)

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


c = Calificaciones()

c.agregar(80, 90, 70, 85)

print(c.calificaciones)
print(c.mayor())
print(c.menor())
print(c.promedio())
