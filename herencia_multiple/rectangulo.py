from figura_geometrica import FiguraGeometrica
from color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        return FiguraGeometrica.get_alto(self) * FiguraGeometrica.get_ancho(self)

    def __str__(self):
        return FiguraGeometrica.__str__(self) + f"\nArea: {str(self.area())}" + Color.__str__(self)
