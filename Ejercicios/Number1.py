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

class Calificador2:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if isinstance(nota, (int, float)) and 0 <= nota <= 100:
            return True
        return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
            else:
                print(f"Aviso: La nota {nota} fue rechazada por ser inválida.")
                
        return self.notas

    def promedio(self):
        cantidad_notas = len(self.notas)
        if cantidad_notas == 0:
            return 0.0
            suma_total = sum(self.notas)
        return suma_total / cantidad_notas

 Prueba = Calificador2()
    notas_aceptadas = Prueba.cargar_notas(85, 105, -5, 90, 100, 45, "A")
    print(calificador2.promedio())   
