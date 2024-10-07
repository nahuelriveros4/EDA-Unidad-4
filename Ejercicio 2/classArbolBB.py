from classNodo import *

class ABB:
    raiz:Nodo
    def __init__(self, raiz=None):
        self.raiz = raiz

    def getRaiz(self):
        return self.raiz
    
    # Insertar un elemento en el árbol binario de búsqueda
    def insertar(self, x):
        if self.raiz is None:
            self.raiz = Nodo(x)
        else:
            nodo_actual = self.raiz
            while nodo_actual is not None:
                if x == nodo_actual.obtener_item():
                    raise ValueError(f"Error: El elemento {x} ya existe en el árbol.")
                elif x < nodo_actual.obtener_item():
                    if nodo_actual.obtener_izq() is None:
                        nodo_actual.cargar_izq(Nodo(x))
                        nodo_actual = None  
                    else:
                        nodo_actual = nodo_actual.obtener_izq()
                else:
                    if nodo_actual.obtener_der() is None:
                        nodo_actual.cargar_der(Nodo(x))
                        nodo_actual = None  
                    else:
                        nodo_actual = nodo_actual.obtener_der()
    # Buscar un elemento en el árbol
    def buscar(self, x):
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if nodo_actual is None:
                raise ValueError(f"Error: Elemento {x} inexistente.")
            if x == nodo_actual.obtener_item():
                return nodo_actual 
            elif x < nodo_actual.obtener_item():
                nodo_actual = nodo_actual.obtener_izq()
            else:
                nodo_actual = nodo_actual.obtener_der() 
        raise ValueError(f"Error: Elemento {x} inexistente.")

    def nodoPadre_Hermano(self, x):
        nodo_actual = self.raiz
        padre = None
        hermano = None
        while nodo_actual is not None:
            if x == nodo_actual.obtener_item():
                if padre is None:
                    print(f"El nodo {x} no tiene padre ni hermano.")
                else:
                    if padre.obtener_izq() == nodo_actual:
                        hermano = padre.obtener_der()
                    else:
                        hermano = padre.obtener_izq()
                    print(f"Padre del nodo {x}: {padre.obtener_item()}")
                    if hermano:
                        print(f"Hermano del nodo {x}: {hermano.obtener_item()}")
                    else:
                        print(f"El nodo {x} no tiene hermano")
                return
            elif x < nodo_actual.obtener_item():
                padre = nodo_actual
                nodo_actual = nodo_actual.obtener_izq()  
            else:
                padre = nodo_actual
                nodo_actual = nodo_actual.obtener_der()
        print(f"Error: el nodo {x} no existe en el arbol")

    # b) Mostrar la cantidad de nodos del árbol en forma recursiva
    def contar_nodos(self, nodo , cont =0):
        if nodo is not None:
            cont += 1
            cont = self.contar_nodos(nodo.obtener_izq(), cont)
            cont = self.contar_nodos(nodo.obtener_der(), cont)
        return cont

    # Calcular la altura del árbol
    def altura(self, nodo):
        if nodo is  None:
            return -1
        else:
            altura_izq = self.altura(nodo.obtener_izq())
            altura_der = self.altura(nodo.obtener_der())
        return 1+max(altura_izq, altura_der)
    
    # d) Mostrar los sucesores de un nodo ingresado previamente
    def sucesores(self, x):
        nodo = self.buscar(x)  
        if nodo.obtener_der() is not None:
            sucesor = nodo.obtener_der()
            while sucesor.obtener_izq() is not None:
                sucesor = sucesor.obtener_izq()
            print(f"El sucesor de {x} es {sucesor.obtener_item()}")
        else:
            print(f"El nodo {x} no tiene sucesor.")
