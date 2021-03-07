class AreaRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Elkin no te olvides: Los inputs siempre pasaran un dato string asi que ponle int() para que sea un numero :v


base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: "))

rectangulo = AreaRectangulo(base, altura)
print("El area del rectangulo es:", rectangulo.area(), "metros.")
