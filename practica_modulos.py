class Utiles:
    def __init__(self, nombre, cantidad, costo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo

    def __str__(self):
        return "BIENVENIDOS A VARIEDADES SULEIDI \n" \
            f"Nombre: {self.nombre} \nCantidad: {str(self.cantidad)} Unidades \nCosto: {str(self.costo)} Pesos"


class UtilesUsados(Utiles):
    def __init__(self, nombre, cantidad, costo, estado):
        super().__init__(nombre, cantidad, costo)
        self.estado = estado

    def __str__(self):
        return super().__str__() + f"\nEstado: {self.estado}"
