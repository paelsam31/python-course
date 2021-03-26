from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figura_geometrica import FiguraGeometrica

# No es posible crear un objeto de una clase abstracta
# figurageometrica = FiguraGeometrica()


cuadrado = Cuadrado(4, "Rojo")
rectangulo = Rectangulo(2, 6, "Verde")
print(cuadrado.area())
print(cuadrado.get_color())
print("U//////////////////////////////////////////////////////////////////////////////////////////////////////////////////U")
print(rectangulo)

# Method Resolution Order
print(Cuadrado.mro())
