class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Hallar el primer punto:")
        x = int(input("Ingresa el valor de X del primer punto: "))
        y = int(input("Ingresa el valor de Y del primer punto: "))
        print("Hallar el segundo punto:")
        x2 = int(input("Ingresa el valor de X del segundo punto: "))
        y2 = int(input("Ingresa el valor de Y del segundo punto: "))

    def PuntoString(self):
        if self.x == None and self.y == None:
            self.x == 0
            self.y == 0
        print(f"Primer Punto: ({self.x},{self.y})")

    def Cuadrante(self):
        if self.x == 0 and self.y != 0:
            print("El cuadrante se situa sobre el eje Y")
        if self.x != 0 and self.y == 0:
            print("El cuadrante se situa en el eje X")
        if self.x == 0 and self.y == 0:
            print("El cuadrante esta sobre el origen")

    def Vector(self):
        print(f"El vector es: ({self.x2 - self.x},{self.y2 - self.y})")

    def Distancia(self):
        import math
        print(
            f"La distancia es: {math.sqrt((self.x2 - self.x)**2 + (self.y2 - self.y)**2)}")


punto = Punto(0, 0)
punto.PuntoString()
print(f"Segundo punto: {(self.x2,self.y2)}")
punto.Vector()
punto.Distancia()
