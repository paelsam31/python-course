class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo que imprime los valores del objeto en string y puede ser heredado
    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Inicializando los valores de la clase padre a la clase hija y definiendo los valores de la clase hija.
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + ", Sueldo: " + str(self.sueldo)


persona = Persona("Elkin", 15)
# Se esta imprimiendo la direccion en memoria del objeto
print(persona)

empleado = Empleado("Elkin", 15, 500.00)
empleado.nombre = "Samir"
empleado.sueldo = 1000.00
print(empleado)
