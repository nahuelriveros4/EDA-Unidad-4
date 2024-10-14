from classNodo import *

class Page:
    def __init__(self, n):
        self.__m = 0  # Número de elementos en la página
        self.__p0 = None  # Puntero a la primera página hija
        self.__e = [Item() for _ in range(2 * n)]  # Arreglo de elementos del árbol

    def get_m(self):
        return self.__m

    def set_m(self, m):
        self.__m = m

    def increment_m(self):
        self.__m += 1

    def get_p0(self):
        return self.__p0

    def set_p0(self, p0):
        self.__p0 = p0

    def get_item(self, index):
        return self.__e[index]

    def set_item(self, index, item):
        self.__e[index] = item
