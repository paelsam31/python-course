"""Calcular el Volumen de una Caja"""


class Caja:

    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def CalcularVolumen(self):
        return self.alto * self.ancho * self.largo


alto = int(input("Ingresa el Alto: "))
ancho = int(input("Ingresa el Ancho: "))
largo = int(input("Ingresa el Largo: "))

volumen = Caja(alto, ancho, largo)
print("El volumen de la caja es:", volumen.CalcularVolumen(), "metros cúbicos.")
