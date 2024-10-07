from classNodo import *  
from classArbolBB import *  

def insertar_elementos(arbol):
    elementos = [10, 5, 15, 3, 7, 12, 18]
    print("Insertando elementos:", elementos)
    for elemento in elementos:
        arbol.insertar(elemento)

def buscarpadrehermano(arbol, x):
    arbol.nodoPadre_Hermano(x)

def contarNodos(arbol):
    print(f"La cantidad de nodos es: {arbol.contar_nodos(arbol.getRaiz())}")

def mostrarAltura(arbol):
    print(f"La altura del arbol es: {arbol.altura(arbol.getRaiz())}")

def sucesor(arbol,x):
    arbol.sucesores(x)


# Ejecutar el programa
if __name__ == "__main__":
    arbol = ABB()

    # Insertar elementos en el árbol
    insertar_elementos(arbol)

    # Buscar Padre y Hermano del nodo x
    buscarpadrehermano(arbol,7)

    # Contar cantidad de nodos
    contarNodos(arbol)

    # Mostrar altura dela arbol
    mostrarAltura(arbol)

    #Mostrar sucesores
    sucesor(arbol, 5)