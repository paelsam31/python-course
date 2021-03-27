from classholamundo import HolaMundo


a = input("Di Hola: ")
b = input("Di Mundo: ")
try:
    resultado = a + b
    if a != "Hola" and b != "Mundo":
        raise HolaMundo("No has puesto Hola Mundo")
except Exception as e:
    print("Ocurrio un error:", e)
    print(type(e))
else:
    print("Hecho!")
    print("Resultado: " + a + " " + b)
