#Mapeo de estudiantes a notas

class RegistroNotas:
    def __init__(self):
        self.estudiantes = {}
    def registrar(self, estudiante, nota):
        self.estudiantes[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        return [estudiante for estudiante, nota in self.estudiantes.items() if nota >= nota_minima]
    def mejor_estudiante(self):
        return max(self.estudiantes.items(), key=lambda x: x[1])[0]

registro = RegistroNotas()
registro.registrar("Juan", 10)
registro.registrar("Pedro", 20)
registro.registrar("Maria", 30)
registro.registrar("Luis", 40)
print(registro.estudiantes_aprobados(30))
print(registro.mejor_estudiante())  