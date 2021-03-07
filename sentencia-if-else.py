condicion = False
''' if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es Falsa")
else:
    print("Escribe un valor booleano") '''

# Sintaxis Simplificada
print("Condicion verdadera") if condicion else print("Condicion Falsa")
#####################################################

numero = int(input("Ingresa un numero entre uno y tres: "))
if numero == 1:
    numeroTexto = "Numero Uno"
elif numero == 2:
    numeroTexto = "Numero Dos"
elif numero == 3:
    numeroTexto = "Numero Tres"
else:
    numeroTexto = "Valor Fuera de Rango"

print("Numero ingresado: ", numeroTexto)
