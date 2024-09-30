class Nodo:
    __item: object
    __izq: object
    __der: object
    def __init__(self, xitem=None, xizq=None, xder=None):
        self.__item=xitem
        self.__izq=xizq
        self.__der=xder
    
    def cargaritem(self, x):
        self.__item = x
        
    def obtener_item(self):
        return self.__item
    
    def cargar_izq(self, nodo):
        self.__izq = nodo

    def obtener_izq(self):
        return self.__izq

    def cargar_der(self, nodo):
        self.__der = nodo

    def obtener_der(self):
        return self.__der