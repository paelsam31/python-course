class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje


class NumerosDivisibles(Exception):
    def __init__(self, mensaje):
        self.message = mensaje
