class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    # A p1 se le asigna self y a p2 el parametro otro
    # Metodo sobreescrito de la clase padre object
    # Funcion para modificar la suma
    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre

    def __sub__(self, otro):
        return "Operacion No Soportada"


p1 = Persona("Juan")
p2 = Persona("Karla")

print(p1 + p2)
print(p1 - p2)
