#Contador de frecuencias

class ContadorFrecuencia:
    def __init__(self):
        self.diccionario = {}
    def agregar_elemento(self, elemento):
        if elemento in self.diccionario:
            self.diccionario[elemento] += 1
        else:
            self.diccionario[elemento] = 1
    def elemento_mas_frecuente(self):
        return max(self.diccionario.items(), key=lambda x: x[1])[0]
    def frecuencia_elemento(self, elemento):
        return self.diccionario[elemento]
contador = ContadorFrecuencia()
contador.agregar_elemento("a")
contador.agregar_elemento("b")
contador.agregar_elemento("c")
contador.agregar_elemento("d")
contador.agregar_elemento("e")
contador.agregar_elemento("a")

print(contador.elemento_mas_frecuente())    
print(contador.frecuencia_elemento("a"))        

#Hecho por mi 
class Contador:

    def __init__(self):
        self.datos = {}

    def agregar(self, dato):
        if dato in self.datos:
            self.datos[dato] += 1
        else:
            self.datos[dato] = 1

    def mas_repetido(self):
        mayor = 0
        resultado = None

        for dato, cantidad in self.datos.items():
            if cantidad > mayor:
                mayor = cantidad
                resultado = dato

        return resultado

    def frecuencia(self, dato):
        if dato in self.datos:
            return self.datos[dato]

        return 0


c = Contador()

c.agregar("Pink")
c.agregar("Blue")
c.agregar("Pink")
c.agregar("Pink")

print(c.datos)
print(c.mas_repetido())
print(c.frecuencia("Pink"))
