#validador de notas con promedio

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)
calificador = Calificador()
print(calificador.cargar_notas(72, 95, 110, 84, -5, 70))
print(calificador.promedio())   

# Hecho por mi 

class Notas:

    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)


notas = Notas()

notas.agregar_nota(80)
notas.agregar_nota(90)
notas.agregar_nota(70)

print(notas.notas)
print(notas.promedio())
