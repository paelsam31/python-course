class Persona:
    def __init__(self, nombre, apePaterno, apeMaterno):
        self.nombre = nombre
        self._apellidoPa = apePaterno
        self.__apellidoMa = apeMaterno

    def get(self):
        return self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellidoPa)
        print(self.__apellidoMa)

    def getMa(self):
        return self.__apellidoMa

    def setMa(self, apeMaterno):
        self.__apellidoMa = apeMaterno


p1 = Persona("Elkin", "Angulo", "Panameño")
p1.get()

print(p1.nombre)
print(p1._apellidoPa)
print(p1.getMa())
p1.setMa("Panamian")
print(p1.getMa())
