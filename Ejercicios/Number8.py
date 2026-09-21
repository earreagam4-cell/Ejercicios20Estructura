#Asignador de equipos

class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        mayor_integrantes = max(self.equipos.values(), key=len)
        return max(mayor_integrantes, key=len)

equipos = Equipos()
equipos.crear_equipo("Equipo 1")
equipos.crear_equipo("Equipo 2")
equipos.crear_equipo("Equipo 3")
equipos.agregar_jugador("Equipo 1", "Jugador 1")
equipos.agregar_jugador("Equipo 1", "Jugador 2")
equipos.agregar_jugador("Equipo 2", "Jugador 3")
equipos.agregar_jugador("Equipo 3", "Jugador 4")
print(equipos.equipo_mayor_integrantes())   

#Hecho por mi 
class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear(self, curso):
        self.cursos[curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor(self):
        mayor = ""
        cantidad = 0

        for curso, estudiantes in self.cursos.items():
            if len(estudiantes) > cantidad:
                cantidad = len(estudiantes)
                mayor = curso

        return mayor


c = Cursos()

c.crear("Python")
c.crear("Java")

c.agregar_estudiante("Python", "Ana")
c.agregar_estudiante("Python", "Luis")
c.agregar_estudiante("Java", "Pedro")

print(c.cursos)
print(c.curso_mayor())
