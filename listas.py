nombres = ["Elkin", "Samir", "James", "Jhon", "Luisa"]
# Conocer el largo de nuestra lista
print(len(nombres))
# Señalar un solo elemento
print(nombres[0])
print(nombres[1])
# Navegacion Inversa
print(nombres[-1])  # El ultimo elemento de la lista
print(nombres[-2])  # El penultimo elemento de la lista
# Imprimir Rango
print(nombres[0:2])  # Inprime los elementos 0 y 1 sin incluir el indice 2
# Imprimir los elementos del inicio hasta el indice proporcionado
print(nombres[:3])  # Sin incluir el indice 3
# Imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])  # Sin incluir el indice 0
# Cambiar los elementos de una lista
nombres[3] = "Panameño"
print(nombres)
# Iterar la lista
for nombre in nombres:
    print(nombre)
# Revisar si existe un elemento en la lista
if "Karla" in nombres:
    print("Karla si existe en la lista")
else:
    print("Karla no existe en la lista")
# Agregar un nuevo elemento
nombres.append("Jorel")
print(nombres)
# Insertar un nuevo elemento en el indice proporcionado
nombres.insert(1, "Angulo")
print(nombres)
# Remover un elemento
nombres.remove("Angulo")
print(nombres)
# Remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)
# Remover el indice indicado de la lista
del nombres[0]
print(nombres)
# Limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)
# Eliminar nuestra lista
del nombres
