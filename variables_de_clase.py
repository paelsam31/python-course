class MiClase:
    variable_clase = "Variable de Clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


# Esta tambien es una variable de Clase (No comparar con la de abajo ya que esa esta modificando el atributo que estaran con los objetos, asocinadolo a su misma clase)
print(MiClase.variable_clase)
objeto1 = MiClase("Variable Instancia")

# Esta variable esta asociada al objeto
print(objeto1.variable_instancia)  # Valores Distintos

# Esta variable esta asociada a la Clase es muy diferente a la del objeto
# NOTA IMPORTANTE: No podemos acceder a las variables de instancia desde las clases, excepto si la quieres modificar
MiClase.variable_instancia = "Modificando Variable de Instancia"
print(MiClase.variable_instancia)  # Valores Distintos

# Podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
# Podemos acceder a las variables de clase con el nombre de la clase
print(MiClase.variable_clase)

# Esta modificacion a la variable de clase solo se asocia al objeto quien lo modifica
# SUPER IMPORTANTE: No modificamos el valor como tal, solo se crea una variable igual dentro del objeto
objeto1.variable_clase = "Modificando Variable de Clase"
print(objeto1.variable_clase)
print(MiClase.variable_clase)

# Si no hacemos una modificacion a la variable de clase, esta seguira teniendo su valor por defecto.
objeto2 = MiClase("Nuevo Valor de Variable de Instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("Tercer Objeto")

# Si modificamos este atributo de clase desde la misma clase, los objetos que no lo modificaron cambian a ese mismo valor. Ejemplo
MiClase.variable_clase = "Cambio desde la Clase"
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)
