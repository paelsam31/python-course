from numeros_identicos import NumerosIdenticosException
from numeros_identicos import NumerosDivisibles

# Manejo de excepciones: CODIGO
resultado = None


try:
  # Preview to the side no soporta los input
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a % b:
        raise NumerosDivisibles(
            "Ocurrio un error, la division tiene residuo.")
    # El objeto "e" apenas se crea, se elimina dando a imprimir el resultado.
    # Para el manejo de errores, primero debemos poner primero las de menor jeraquia, la utilima es la exception mayor, es decir, Exception
except ZeroDivisionError as e:
    print("Ocurrio un error con ZeroDivisionError:", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TypeError:", e)
    print(type(e))
# except ValueError as e:
#    print("Ocurrio un error con ValueError", e)
#    print(type(e))
except Exception as e:
    print("Ocurrio un error con Excepcion:", e)
    print(type(e))
# Si no ocurre ningun error(Es opcional)
else:
    print("No hay excepciones")
# Finally siempre se ejecutara, sin importar que fue error o exito (Es opcional)
finally:
    print("Fin del manejo de excepciones")


print("Resultado:", resultado)
print("Continua...")
