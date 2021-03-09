class Producto:
    def __init__(self, nombre, numero, vencimiento):
        self.nombre = nombre
        self.numeroDeSerie = numero
        self.vencimiento = vencimiento

    # "\" Es como una coma para saltar codigo
    def __str__(self):
        return f"Nombre del Producto: {self.nombre} \n" \
            f"Numero de Serie: {str(self.numeroDeSerie)} \n" \
            f"Fecha de Vencimiento: {str(self.vencimiento)}"


class Electronicos(Producto):
    def __init__(self, nombre, numero, vencimiento, uso):
        super().__init__(nombre, numero, vencimiento)
        self.uso = uso

    def __str__(self):
        return super().__str__() + f"\nUso: {self.uso}"


atun = Producto("Rosalinda", 20430, 2022)
print(atun)
print("\n")
print("///////////////////////////////////////////////////////////////////////\n")
computador = Electronicos("ASUS", 2050, None, "Trabajo")
print(computador)
