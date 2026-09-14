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