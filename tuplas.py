frutas = (
    "Fresas",
    "Manzanas",
    "Naranjas",
    "Platano"
)
print(frutas)

# Largo de la tupla
print(len(frutas))
# Accediendo a un elemento
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Rangos
print(frutas[0:2])  # Excluyendo el indice 2
# No podemos modificar un valor
""" frutas[0] = "Pera " """
# Hacer cambios en Tuplas convirtiendola en lista
frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print(frutas)
# Iterar una tupla
for fruta in frutas:
    print(fruta, end=", ")
# No podemos agregar ni eliminar elementos de una tupla
""" del frutas
print(frutas) """
