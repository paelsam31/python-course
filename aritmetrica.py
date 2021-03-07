class Aritmetrica:
    """Clase aritmetrica para realizar las operaciones suma resta, etc"""

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multi(self):
        return self.operando1 * self.operando2

    def div(self):
        return self.operando1 / self.operando2

    def pot(self):
        return self.operando1 ** self.operando2


# Creando un nuevo objeto
suma = Aritmetrica(2, 2)
print("Resultado:", suma.sumar())
resta = Aritmetrica(2, 2)
print("Resultado:", resta.restar())
multiplicacion = Aritmetrica(2, 2)
print("Resultado:", multiplicacion.multi())
division = Aritmetrica(2, 2)
print("Resultado:", int(division.div()))
potencia = Aritmetrica(2, 2)
print("Resultado:", potencia.pot())
