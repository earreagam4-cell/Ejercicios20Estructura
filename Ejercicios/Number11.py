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
