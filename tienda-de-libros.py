print("Proporcione los siguientes datos del libro")
nombre = input("Ingresa el nombre del libro: ")
id = int(input("Ingrsa el ID del libro: "))
precio = float(input("Ingresa el precio del libro: "))
envioGratuito = input("El envio es gratuito? (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Ingresa un valor valido (True/False)"

print("Nombre:", nombre)
print("Id:", id)
print("Precio:", precio)
print("Envio Gratuito:", envioGratuito)


print(type(envioGratuito))
