# Hallar el area de un triangulo
class Triangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def areaTriangulo(self):
        return (self.base * self.altura) / 2


base = int(input("Ingresa la base del triangulo: "))
altura = int(input("Ingresa la altura del triangulo: "))

triangulo = Triangulo(base, altura)
print("El area del triangulo es:", int(
    triangulo.areaTriangulo()), "metros cubicos")
