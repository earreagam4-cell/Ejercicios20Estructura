#Analizador de patrones en textos

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = {}
    def encontrar_palabras(self, texto, patron):
        return [palabra for palabra in texto.split() if palabra.startswith(patron)]
    def agrupar_por_longitud(self, texto):
        self.palabras = {}
        for palabra in texto.split():
            if len(palabra) not in self.palabras:
                self.palabras[len(palabra)] = []
            self.palabras[len(palabra)].append(palabra)
        return self.palabras
    def palabras_unicas(self):
        return set(self.palabras.values())

analizador = AnalizadorPatrones()
print(analizador.encontrar_palabras("hola hola adios adios", "hola"))
print(analizador.agrupar_por_longitud("hola hola adios adios"))
print(analizador.palabras_unicas())     

# Hecho por mi 

class Buscador:

    def __init__(self):
        self.palabras = []

    def buscar(self, texto, inicio):

        resultado = []

        for palabra in texto.split():

            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar(self, texto):

        resultado = {}

        for palabra in texto.split():

            largo = len(palabra)

            if largo not in resultado:
                resultado[largo] = []

            resultado[largo].append(palabra)

        return resultado

    def unicas(self):

        return set(self.palabras)


b = Buscador()

texto = "casa carro perro casa"

print(b.buscar(texto, "ca"))

print(b.agrupar(texto))

b.palabras = texto.split()

print(b.unicas())
