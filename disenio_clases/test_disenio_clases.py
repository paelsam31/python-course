from orden import Orden
from producto import Producto

producto1 = Producto("Camisa", 200)
producto2 = Producto("Pantalon", 250)
producto3 = Producto("Zapatos", 230)
producto4 = Producto("Cadena", 50)

productos = [producto1, producto2]

# orden1 = Orden(productos)
# print(orden1)

orden2 = Orden(productos)
orden2.agregar_productos(producto3)
orden2.agregar_productos(producto4)
print(orden2)
