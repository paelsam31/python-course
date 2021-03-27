from empleado import Empleado
from gerente import Gerente


# Este metodo puede apuntar a cualquier clase sea padre o hija.
def imprimit_detalles(objeto):
    print(objeto)
    print(type(objeto), end="\n\n")
    # Isnstance: Es un metodo para saber si un atributo esta en un objeto de clase
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Elkin", 1000.00)
imprimit_detalles(empleado)

empleado = Gerente("Luisa", 2000.00, "Sitemas")
imprimit_detalles(empleado)
