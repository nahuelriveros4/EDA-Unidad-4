# El nodo contiene:
# EL CARACTER
# LA FRECUENCIA
# Puntero al nodo izquierdo y derecho

class Nodo:
    __caracter: str
    __frecuencia: int
    __izquierda: object
    __derecha: object
    def __init__(self, caracter, frecuencia):
        self.__caracter=caracter
        self.__frecuencia = frecuencia
        self.__izquierda = None
        self.__derecha = None

    def get_caracter(self):
        return self.__caracter
    
    def get_frecuencia(self):
        return self.__frecuencia
    
    def set_izq(self, izq):
        self.__izquierda = izq

    def set_der(self, der):
        self.__derecha = der

    def get_izq(self):
        return self.__izquierda
    
    def get_der(self):
        return self.__derecha

    def es_hoja(self):
        return self.__izquierda is None and self.__derecha is None

    