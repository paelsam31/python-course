class Vehiculo:
    def __init__(self, nombre, numeroRuedas):
        self.nombre = nombre
        self.numeroRuedas = numeroRuedas

    def __str__(self):
        return "Nombre: " + self.nombre + ", Numero de ruedas: " + str(self.numeroRuedas) + " ruedas"


class Coche(Vehiculo):
    def __init__(self, nombre, numeroRuedas, velocidad):
        super().__init__(nombre, numeroRuedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad: " + str(self.velocidad) + "Km/h"


class Bicicleta(Vehiculo):
    def __init__(self, nombre, numeroRuedas, tipoCadenas):
        super().__init__(nombre, numeroRuedas)
        self.tipoCadenas = tipoCadenas

    def __str__(self):
        return super().__str__() + ", Tipo de Cadena: " + self.tipoCadenas


coche = Coche("Chavored", 4, 20)
print(coche)

bici = Bicicleta("Bicicleta: BMX", 2, "Grande")
print(bici)
