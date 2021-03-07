# Set es una coleccion sin orden y sin indices, no permite elementos repetidos y los elementos elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {
    "Marte",
    "Jupiter",
    "Venus"
}
print(planetas)
# Largo
print(len(planetas))
# Si un elemento esta presente
print("Tierra" in planetas)
# Agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")  # No se puede agregar elementos duplicados
# Eliminar un elemento
# Eliminar con remove posiblemente arroja excepcion
planetas.remove("Tierra")
print(planetas)
# Eliminar con discard no arroja una excepcion
planetas.discard("Jupiter")
print(planetas)
# Limpiar el set completamente
planetas.clear()
print(planetas)
# Eliminar el set
del planetas
print(planetas)
