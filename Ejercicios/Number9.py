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