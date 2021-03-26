class MiClase:

    variable_clase = "Varible Clase"

    def __init__(self):
        self.varible_instancia = "Variable Instancia"

    # Los decoradores agregan funcionalidad a los metodos, en este caso vamos a hacer un metodo estatico.
    @staticmethod
    # Este metodo se asocia a nuestra clase, no a los objetos.
    # Este metodo no puede recibir parametro self porque eso es solo para los objetos
    def metodo_estatico():
        print("Metodo Estatico")
        # No podemos acceder a variables de clase. Excepto si utilizamos el nombre de la clase con la variable.
        print(MiClase.variable_clase)
        # Se debe crear un objeto para entrar a las variables de intancia.
        # print(MiClase.variable_instancia)

    # Esta es otra forma de crear un metodo de clase. Este si debe recibir parametros.
    # cls es el nombre de la clase. Puede ser cualquier otro nombre, pero ese nombre es comun.
    @classmethod
    def metodo_clase(cls):
        print("Metodo de Clase: " + str(cls))
        # Comparado con @staticmethod, en este podemos utilizar el parametro que tiene para llamar a la variable de clase.
        print(cls.variable_clase)
        # Se debe crear un objeto para entrar a las variables de intancia.
        # print(cls.varible_instancia)

    # Con este metodo podemos accedear a cualquier metodo de la clase
    # Nota el contexto estatico no puede acceder a el contexto dinamico pero el dinamico puede acceder al estatico (Contexto dinamico: metodo_instancia).
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.varible_instancia)
        print(self.variable_clase)


print()
objeto1 = MiClase()
objeto1.metodo_instancia()

# Asi llamamos a los metodos de las clases.
MiClase.metodo_estatico()
MiClase.metodo_clase()
