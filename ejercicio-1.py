base = int(input("Ingresa la base del rectangulo: "))
altura = int(input("Ingresa la altura del rectangulo: "))
perimetro = (base * 2) + (altura * 2)
area = base * altura

print("El perimetro del rectangulo:", perimetro, "metros.")
print("El area del rectangulo:", area, "metros cuadrados.")

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
else:
    print(num2, "es mayor que", num1)
