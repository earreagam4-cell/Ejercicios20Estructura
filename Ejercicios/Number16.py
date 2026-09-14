#Codificador/Decodificador

class CodificadorCesar:
    def __init__(self):
        self.codificaciones = []
    def codificar_letra(self, letra, desplazamiento):
        return chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        return codificada
    def codificar_multiples(self, palabras, desplazamiento):
        resultado = {}
        for palabra in palabras:
            resultado[palabra] = self.codificar_palabra(palabra, desplazamiento)
        return resultado
codificador = CodificadorCesar()
print(codificador.codificar_multiples(["hola", "adios", "buenos dias"], 3))     