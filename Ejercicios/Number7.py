#Mapeador de edades

class GestorPersonas:
    def __init__(self):
        self.personas = {}
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]
    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)
gestor = GestorPersonas()
gestor.agregar_persona("Juan", 20)
gestor.agregar_persona("Pedro", 30)
gestor.agregar_persona("Maria", 40)
gestor.agregar_persona("Luis", 50)
print(gestor.personas_mayores(30))
print(gestor.edad_promedio())   