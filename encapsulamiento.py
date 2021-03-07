class Persona:
    def __init__(self, n, edad):
        self.__nombre = n
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Juan", 18)
# print(p1.__nombre) Marca un error
print(p1.get_nombre())
print(p1.get_edad())

# p1.__nombre = "Elkin" Marca un error
p1.set_nombre("ELKIN")
p1.set_edad(20)
print(p1.get_edad())
print(p1.get_nombre())
