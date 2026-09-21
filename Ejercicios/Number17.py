#Grupo de edades

class AgrupadorEdades:
    def __init__(self):
        self.categorias = {}
    def clasificar_edad(self, edad):
        if edad < 18:
            return "niño"
        elif edad < 25:
            return "adolescente"
        elif edad < 35:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            cat = self.clasificar_edad(edad)
            if cat not in self.categorias:
                self.categorias[cat] = []
            self.categorias[cat].append(edad)
        
        return self.categorias
    def edad_promedio_categoria(self, categoria):
        if categoria in self.categorias and len(self.categorias[categoria]) > 0:
            lista_edades = self.categorias[categoria]
            return sum(lista_edades) / len(lista_edades)
        return 0
agrupador = AgrupadorEdades()
agrupador.agrupar_por_categoria(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(agrupador.edad_promedio_categoria("adolescente"))

# Hecho por mi 

class Clasificador:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "joven": [],
            "adulto": []
        }

    def clasificar(self, edad):

        if edad < 13:
            return "niño"

        elif edad < 18:
            return "joven"

        else:
            return "adulto"

    def agrupar(self, *edades):

        for edad in edades:
            grupo = self.clasificar(edad)
            self.grupos[grupo].append(edad)

        return self.grupos


c = Clasificador()

print(c.agrupar(10, 15, 20, 30))
