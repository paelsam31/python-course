from producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    def agregar_productos(self, producto):
        if len(self.__productos) <= 2:
            self.__productos.append(producto)
        else:
            print("NUMERO MAXIMO DE PRODUCTOS. SOLO SE ACEPTAN 3 PRODUCTOS")

    def calcular_total(self):
        total = 0
        for precio in self.__productos:
            total += precio.get_precio()
        return total

    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + f"\n\n"
        return "\nOrden: " + str(self.__id_orden) + "\n\nProductos: \n\n" + productos_str + f"\n\nTotal a pagar: {str(self.calcular_total())}"
