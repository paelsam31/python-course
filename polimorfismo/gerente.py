from empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        Empleado.__init__(self, nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return Empleado.__str__(self) + "\nDepartamento: " + self.departamento
