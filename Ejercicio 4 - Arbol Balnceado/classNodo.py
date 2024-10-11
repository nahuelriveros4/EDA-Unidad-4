class NodoAVL:
    def __init__(self, key):
        self.__key = key
        self.__con = 1  # Contador de ocurrencias del nodo
        self.__bal = 0  # Factor de balance
        self.__izq = None  # Hijo izquierdo
        self.__der = None  # Hijo derecho

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_con(self):
        return self.__con

    def set_con(self, con):
        self.__con = con

    def get_bal(self):
        return self.__bal

    def set_bal(self, bal):
        self.__bal = bal

    def get_izq(self):
        return self.__izq

    def set_izq(self, izq):
        self.__izq = izq

    def get_der(self):
        return self.__der

    def set_der(self, der):
        self.__der = der
