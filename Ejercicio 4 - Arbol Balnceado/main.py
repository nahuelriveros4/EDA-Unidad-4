from classArbolAVL import ArbolAVL


if __name__ == "__main__":
    arbol = ArbolAVL()
    h = [0]  # Para llevar el control de la altura

    # Insertar las claves: 7, 5, 2, 4, 3, 8, 1, 6, 11, 10, 9
    claves_insertar = [7, 5, 2, 4, 3, 8, 1, 6, 11, 10, 9]
    for clave in claves_insertar:
        arbol.set_raiz(arbol.insertar(arbol.get_raiz(), clave, h))

    print("Árbol AVL después de insertar:")
    arbol.preorden(arbol.get_raiz())
    print()

    # Suprimir las claves: 4, 8, 6, 5, 2, 1, 7
    claves_eliminar = [4, 8, 6, 5, 2, 1, 7]
    for clave in claves_eliminar:
        arbol.set_raiz(arbol.eliminar(arbol.get_raiz(), clave, h))

    print("Árbol AVL después de eliminar:")
    arbol.preorden(arbol.get_raiz())
