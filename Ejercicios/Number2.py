#Contador de palabras únicas

class AnalizadorTexto:
    def __init__(self):
        self.palabras = set()
        self.palabras_ordenadas = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras:
            self.palabras.add(palabra)
            self.palabras_ordenadas.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

analizador = AnalizadorTexto()
analizador.agregar_multiples("hola", "hola", "adios", "adios", "adios", "hola")
print(analizador.contar_palabras())
print(analizador.palabras_ordenadas) 

#Hecho por mi 
class Frutas:

    def __init__(self):
        self.frutas = []
        self.unicas = set()

    def agregar(self, fruta):
        self.frutas.append(fruta)
        self.unicas.add(fruta)

    def agregar_muchas(self, *frutas):
        for fruta in frutas:
            self.agregar(fruta)

    def cantidad(self):
        return len(self.unicas)


f = Frutas()

f.agregar_muchas("manzana", "pera", "manzana", "uva")

print(f.frutas)
print(f.unicas)
print(f.cantidad())
