# Definiendo la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Modificando los valores
Persona.nombre = "Elkin"
Persona.edad = 15

# Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

# Crear un nuevo objeto
persona = Persona("Karla", 30)
print(persona.nombre)
print(persona.edad)
print(id(persona))

# Creando un segundo objeto

persona2 = Persona("Carlos", 40)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))
