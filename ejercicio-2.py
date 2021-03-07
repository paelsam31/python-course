# Ejercicio hecho a base del sistema de calificacion de mi escuela

estudianteCalificacion = float(
    input("Ingresa tu calificación (Entre 1.0 y 5.0): "))
resultado = None

if estudianteCalificacion <= 2.9 and estudianteCalificacion >= 1.0:
    resultado = "Tu calificacion es baja, perdiste"
elif estudianteCalificacion <= 3.9 and estudianteCalificacion >= 3.0:
    resultado = "Tu calificacion es basica, pero ganaste"
elif estudianteCalificacion <= 5.0 and estudianteCalificacion >= 4.0:
    resultado = "Tu calificacion es alta, ganaste"
else:
    resultado = "Ingresa un valor correcto (Entre 1.0 y 5.0)"

print(resultado)
