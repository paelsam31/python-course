# Un diccionario esta compuesto de llave, valor (key, value)
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OPP": "Objet Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)
# Largo
print(len(diccionario))
# Accediendo a un elemento
print(diccionario["IDE"])
# Otra forma, mismo resultado
print(diccionario.get("IDE"))
# Modificando Valores
diccionario["IDE"] = "Integrated development enviroment"
print(diccionario)
# Iterar
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])

for valor in diccionario.values():
    print(valor)

# Comprobando existencia de un elemento
print("IDE" in diccionario)

# Agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)
# Remover elementos
diccionario.pop("DBMS")
print(diccionario)

#Limpiar el diccionario
diccionario.clear()
print(diccionario)

#Eliminar por completo
del diccionario
print(diccionario)