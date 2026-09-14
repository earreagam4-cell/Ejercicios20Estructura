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