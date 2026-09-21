#Validador de caracteres

class AnalizadorString:     
    def __init__(self, texto):
        self.texto = texto
        self.longitud = len(texto)
        self.tipo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
    def solo_vocales(self, letra):
        return letra in 'aeiou'
    def contar_por_tipo(self, texto):
        for letra in texto:
            if self.solo_vocales(letra):
                self.tipo['vocales'] += 1
            else:
                self.tipo['consonantes'] += 1
        self.tipo['digitos'] = self.longitud - self.tipo['vocales'] - self.tipo['consonantes']
        return self.tipo
    def mas_largo(self):
        return max(self.tipo.values())
analizador = AnalizadorString("hola")
print(analizador.contar_por_tipo("hola"))
print(analizador.mas_largo())       

#Hecho por mi


    def __init__(self):
        self.texto_largo = ""

    def es_vocal(self, letra):
        return letra.lower() in "aeiou"

    def contar(self, texto):
        vocales = 0
        consonantes = 0
        numeros = 0

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        for letra in texto:

            if letra.isdigit():
                numeros += 1

            elif letra.isalpha():

                if self.es_vocal(letra):
                    vocales += 1
                else:
                    consonantes += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "numeros": numeros
        }


l = Letras()

print(l.contar("Casa123"))
print(l.texto_largo)
