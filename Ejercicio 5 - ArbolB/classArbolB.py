from classNodo import *
from classPage import *

class BTree:
    def __init__(self, n):
        self.__root = None
        self.__n = n  # Orden del árbol B

    def insertar(self, x):
        h = [False]
        v = [Item()]
        self.__insertar_aux(x, self.__root, h, v)
        if h[0]:
            new_root = Page(self.__n)
            new_root.set_m(1)
            new_root.set_p0(self.__root)
            new_root.set_item(0, v[0])
            self.__root = new_root

    def __insertar_aux(self, x, a, h, v):
        if a is None:  # Nodo vacío
            h[0] = True
            v[0] = Item(x)
        else:
            l, r = 0, a.get_m()
            while l < r:
                i = (l + r) // 2
                if a.get_item(i).get_key() <= x:
                    l = i + 1
                else:
                    r = i
            r -= 1
            if r >= 0 and a.get_item(r).get_key() == x:
                a.get_item(r).increment_count()
                h[0] = False
            else:
                if r < 0 or a.get_item(r).get_key() > x:
                    self.__insertar_aux(x, a.get_p0(), h, v)
                else:
                    self.__insertar_aux(x, a.get_item(r).get_p(), h, v)

                if h[0]:
                    if a.get_m() < 2 * self.__n:
                        h[0] = False
                        a.increment_m()
                        for i in range(a.get_m() - 1, r + 1, -1):
                            a.set_item(i, a.get_item(i - 1))
                        if r < 0 or a.get_item(r).get_key() > x:
                            a.set_item(r, v[0])
                        else:
                            a.set_item(r + 1, v[0])
                    else:
                        self.__split_node(a, v, r, x, h)

    def __split_node(self, a, v, r, x, h):
        b = Page(self.__n)
        if r <= self.__n:
            for i in range(self.__n):
                b.set_item(i, a.get_item(i + self.__n))
            if r == self.__n:
                v[0] = a.get_item(self.__n)
                b.set_item(0, Item(x))
            else:
                if a.get_item(self.__n - 1).get_key() < x:
                    v[0] = Item(x)
                else:
                    v[0] = a.get_item(self.__n - 1)
                    for i in range(self.__n - 1, r, -1):
                        a.set_item(i, a.get_item(i - 1))
                    a.set_item(r, Item(x))
        else:
            r -= self.__n
            v[0] = a.get_item(self.__n)
            for i in range(r):
                b.set_item(i, a.get_item(i + self.__n + 1))
            b.set_item(r, Item(x))
            for i in range(r + 1, self.__n):
                b.set_item(i, a.get_item(i + self.__n))
        a.set_m(self.__n)
        b.set_m(self.__n)
        b.set_p0(v[0].get_p())
        v[0].set_p(b)

    def suprimir(self, x):
        h = [False]
        self.__suprimir_aux(x, self.__root, h)
        if h[0] and self.__root.get_m() == 0:
            self.__root = self.__root.get_p0()

    def __suprimir_aux(self, x, a, h):
        # Implementar la lógica para suprimir nodos y manejar underflows si es necesario
        pass

    def mostrar(self):
        self.__mostrar_aux(self.__root, 0)

    def __mostrar_aux(self, p, niv):
        if p is not None:
            print("\n" + " " * niv, end="")
            for i in range(p.get_m()):
                print(p.get_item(i).get_key(), end=" ")
            print()
            self.__mostrar_aux(p.get_p0(), niv + 1)
            for i in range(p.get_m()):
                self.__mostrar_aux(p.get_item(i).get_p(), niv + 1)
