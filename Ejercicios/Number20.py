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