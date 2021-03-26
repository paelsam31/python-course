
class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self.__id_producto = Producto.contador_producto
        self.__nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def __str__(self):
        return f"Id Producto: {str(self.__id_producto)}\nNombre: {self.__nombre}\nPrecio: {str(self.__precio)}"
