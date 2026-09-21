#Gestor de tareas con prioridad

class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))
    def tareas_prioritarias(self):
        return [tarea for tarea in self.tareas if tarea[1] == 1]
    def eliminar_completada(self, descripcion):
        self.tareas.remove((descripcion, 1))

tareas = Tareas()
tareas.agregar_tarea("Tarea 1", 1)
tareas.agregar_tarea("Tarea 2", 2)
tareas.agregar_tarea("Tarea 3", 3)
tareas.agregar_tarea("Tarea 4", 4)
tareas.agregar_tarea("Tarea 5", 5)

print(tareas.tareas_prioritarias())
tareas.eliminar_completada("Tarea 1")
print(tareas.tareas_prioritarias())

#Hecho por mi

class Compras:

    def __init__(self):
        self.compras = []

    def agregar(self, producto, cantidad):
        self.compras.append((producto, cantidad))

    def mayores(self):
        resultado = []

        for compra in self.compras:
            if compra[1] >= 3:
                resultado.append(compra)

        return resultado

    def eliminar(self, producto):
        for compra in self.compras:
            if compra[0] == producto:
                self.compras.remove(compra)
                return


c = Compras()

c.agregar("Bread", 5)
c.agregar("Milk", 2)
c.agregar("Rice", 4)

print(c.compras)
print(c.mayores())

c.eliminar("Bread")

print(c.compras)
