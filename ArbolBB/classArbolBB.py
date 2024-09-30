from classNodo import *

class ABB:
    raiz:Nodo
    def __init__(self, raiz=None):
        self.raiz = raiz

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

    def suprimir(self, x):
        if self.raiz is None:
            raise ValueError(f"Error: El árbol está vacío.")
        nodo_actual = self.raiz
        padre = None
        while nodo_actual is not None:
            if x < nodo_actual.obtener_item(): 
                padre = nodo_actual
                nodo_actual = nodo_actual.obtener_izq()
            elif x > nodo_actual.obtener_item():  
                padre = nodo_actual
                nodo_actual = nodo_actual.obtener_der()
            else:
                if nodo_actual.obtener_izq() is None and nodo_actual.obtener_der() is None:
                    if padre is None:  
                        self.raiz = None
                    elif padre.obtener_izq() == nodo_actual:
                        padre.cargar_izq(None)
                    else:
                        padre.cargar_der(None)
                elif nodo_actual.obtener_izq() is None: 
                    if padre is None:  
                        self.raiz = nodo_actual.obtener_der()
                    elif padre.obtener_izq() == nodo_actual:
                        padre.cargar_izq(nodo_actual.obtener_der())
                    else:
                        padre.cargar_der(nodo_actual.obtener_der())
                
                elif nodo_actual.obtener_der() is None: 
                    if padre is None:  
                        self.raiz = nodo_actual.obtener_izq()
                    elif padre.obtener_izq() == nodo_actual:
                        padre.cargar_izq(nodo_actual.obtener_izq())
                    else:
                        padre.cargar_der(nodo_actual.obtener_izq())
                else:
                    sucesor = nodo_actual.obtener_der()
                    sucesor_padre = nodo_actual
                    while sucesor.obtener_izq() is not None: 
                        sucesor_padre = sucesor
                        sucesor = sucesor.obtener_izq()
                    nodo_actual.cargaritem(sucesor.obtener_item())
                    if sucesor_padre.obtener_izq() == sucesor: 
                        sucesor_padre.cargar_izq(sucesor.obtener_der())
                    else:  
                        sucesor_padre.cargar_der(sucesor.obtener_der())
                return  # Elemento eliminado
        raise ValueError(f"Error: Elemento {x} inexistente.")

    # Calcular el nivel del nodo con clave X
    def nivel(self, x):
        nodo_actual = self.raiz
        nivel_actual = 0
        while nodo_actual is not None:
            if nodo_actual.obtener_item() == x:
                return nivel_actual
            elif x < nodo_actual.obtener_item():
                nodo_actual = nodo_actual.obtener_izq()
            else:
                nodo_actual = nodo_actual.obtener_der()
            nivel_actual += 1
        raise ValueError(f"El elemento {x} no está en el árbol.")

    # Evaluar si el nodo con clave X es hoja
    def hoja(self, x):
        nodo = self.buscar(x)
        return nodo.obtener_izq() is None and nodo.obtener_der() is None

    # Evaluar si X es hijo de Z
    def hijo(self, x, z):
        nodo_z = self.buscar(z)
        if (nodo_z.obtener_izq() and nodo_z.obtener_izq().obtener_item() == x) or \
            (nodo_z.obtener_der() and nodo_z.obtener_der().obtener_item() == x):
            return True
        return False

    # Evaluar si Z es padre de X
    def padre(self, x, z):
        return self.hijo(x, z)

    # Recuperar el camino de X a Z
    def camino(self, x, z):
        nodo_x = self.buscar(x)
        nodo_z = self.buscar(z)
        camino = []
        nodo_actual = self.raiz
        while nodo_actual is not None:
            camino.append(nodo_actual.obtener_item())
            if nodo_actual.obtener_item() == z:
                return camino
            elif z < nodo_actual.obtener_item():
                nodo_actual = nodo_actual.obtener_izq()
            else:
                nodo_actual = nodo_actual.obtener_der()
        raise ValueError(f"No hay camino entre {x} y {z}.")

    # Calcular la altura del árbol
    def altura(self):
        if self.raiz is None:
            return -1
        nodo_actual = self.raiz
        stack = [(nodo_actual, 0)]
        max_altura = -1
        while stack:
            nodo, altura_actual = stack.pop()
            if nodo is not None:
                max_altura = max(max_altura, altura_actual)
                stack.append((nodo.obtener_izq(), altura_actual + 1))
                stack.append((nodo.obtener_der(), altura_actual + 1))

        return max_altura

    def preorden(self):
        def _preorden(nodo):
            if nodo is not None:
                print(nodo.obtener_item(), end=' ')  
                _preorden(nodo.obtener_izq()) 
                _preorden(nodo.obtener_der()) 
        print("Preorden:", end=' ')
        _preorden(self.raiz)
        print()

    def inorden(self):
        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.obtener_izq()) 
                print(nodo.obtener_item(), end=' ') 
                _inorden(nodo.obtener_der())  
        print("Inorden:", end=' ')
        _inorden(self.raiz)
        print()

    def postorden(self):
        def _postorden(nodo):
            if nodo is not None:
                _postorden(nodo.obtener_izq())  
                _postorden(nodo.obtener_der())  
                print(nodo.obtener_item(), end=' ')  
        
        print("Postorden:", end=' ')
        _postorden(self.raiz)
        print()