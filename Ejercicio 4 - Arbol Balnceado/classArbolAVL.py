from classNodo import *
class ArbolAVL:
    __raiz: NodoAVL
    def __init__(self):
        self.__raiz = None

    def insertar(self, nodo, clave, altura):
        if nodo is None:  # Insertar nuevo nodo
            nodo = NodoAVL(clave)
            altura[0] = 1
        elif clave < nodo.get_key():
            nodo.set_izq(self.insertar(nodo.get_izq(), clave, altura))
            if altura[0]:  # Si la rama izquierda creció
                if nodo.get_bal() == 1:
                    nodo.set_bal(0)
                    altura[0] = 0
                elif nodo.get_bal() == 0:
                    nodo.set_bal(-1)
                elif nodo.get_bal() == -1:  # Rebalancear
                    nodo = self.rotar_izquierda(nodo, altura)
        elif clave > nodo.get_key():
            nodo.set_der(self.insertar(nodo.get_der(), clave, altura))
            if altura[0]:  # Si la rama derecha creció
                if nodo.get_bal() == -1:
                    nodo.set_bal(0)
                    altura[0] = 0
                elif nodo.get_bal() == 0:
                    nodo.set_bal(1)
                elif nodo.get_bal() == 1:  # Rebalancear
                    nodo = self.rotar_derecha(nodo, altura)
        else:
            nodo.set_con(nodo.get_con() + 1)  # El nodo ya existe, se incrementa el contador
        return nodo

    def rotar_izquierda(self, nodo, altura):
        nodo_izq = nodo.get_izq()
        if nodo_izq.get_bal() == -1:  # Rotación simple lado izquierdo
            nodo.set_izq(nodo_izq.get_der())
            nodo_izq.set_der(nodo)
            nodo.set_bal(0)
            nodo = nodo_izq
        else:  # Rotación doble lado derecho
            nodo_der = nodo_izq.get_der()
            nodo_izq.set_der(nodo_der.get_izq())
            nodo_der.set_izq(nodo_izq)
            nodo.set_izq(nodo_der.get_der())
            nodo_der.set_der(nodo)
            if nodo_der.get_bal() == -1:
                nodo.set_bal(1)
            else:
                nodo.set_bal(0)
            if nodo_der.get_bal() == 1:
                nodo_izq.set_bal(-1)
            else:
                nodo_izq.set_bal(0)
            nodo = nodo_der
        nodo.set_bal(0)
        altura[0] = 0
        return nodo

    def rotar_derecha(self, nodo, altura):
        nodo_der = nodo.get_der()
        if nodo_der.get_bal() == 1:  # Rotación simple lado derecho
            nodo.set_der(nodo_der.get_izq())
            nodo_der.set_izq(nodo)
            nodo.set_bal(0)
            nodo = nodo_der
        else:  # Rotación doble lado izquierdo
            nodo_izq = nodo_der.get_izq()
            nodo_der.set_izq(nodo_izq.get_der())
            nodo_izq.set_der(nodo_der)
            nodo.set_der(nodo_izq.get_izq())
            nodo_izq.set_izq(nodo)
            if nodo_izq.get_bal() == 1:
                nodo.set_bal(-1)
            else:
                nodo.set_bal(0)
            if nodo_izq.get_bal() == -1:
                nodo_der.set_bal(1)
            else:
                nodo_der.set_bal(0)
            nodo = nodo_izq
        nodo.set_bal(0)
        altura[0] = 0
        return nodo

    def eliminar(self, nodo, clave, altura):
        if nodo is None:
            print(f"La llave {clave} no está en el árbol")
        elif clave < nodo.get_key():
            nodo.set_izq(self.eliminar(nodo.get_izq(), clave, altura))
            if altura[0]:
                nodo = self.balancear_derecha(nodo, altura)
        elif clave > nodo.get_key():
            nodo.set_der(self.eliminar(nodo.get_der(), clave, altura))
            if altura[0]:
                nodo = self.balancear_izquierda(nodo, altura)
        else:  # Eliminar nodo encontrado
            nodo_tmp = nodo
            if nodo_tmp.get_der() is None:
                nodo = nodo_tmp.get_izq()
                altura[0] = 1
            elif nodo_tmp.get_izq() is None:
                nodo = nodo_tmp.get_der()
                altura[0] = 1
            else:
                nodo.set_izq(self.sup(nodo_tmp.get_izq(), altura)[0])
                nodo.set_key(nodo_tmp.get_key())
                nodo.set_con(nodo_tmp.get_con())
                if altura[0]:
                    nodo = self.balancear_derecha(nodo, altura)
        return nodo

    def sup(self, nodo, altura):
        if nodo.get_der() is not None:
            nodo.set_der(self.sup(nodo.get_der(), altura)[0])
            nodo = self.balancear_izquierda(nodo, altura)
        else:
            nodo_sup = nodo
            nodo = nodo.get_izq()
            altura[0] = 1
        return nodo, nodo_sup

    def balancear_derecha(self, nodo, altura):
        nodo_der = nodo.get_der()
        if nodo_der and nodo_der.get_bal() == 0:
            nodo_der.set_bal(-1)
            altura[0] = 0
        else:
            nodo_der.set_bal(0)
        return nodo_der

    def balancear_izquierda(self, nodo, altura):
        nodo_izq = nodo.get_izq()
        if nodo_izq and nodo_izq.get_bal() == 0:
            nodo_izq.set_bal(1)
            altura[0] = 0
        else:
            nodo_izq.set_bal(0)
        return nodo_izq

    def preorden(self, nodo):
        if nodo:
            print(nodo.get_key(), end=" ")
            self.preorden(nodo.get_izq())
            self.preorden(nodo.get_der())

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, raiz):
        self.__raiz = raiz
