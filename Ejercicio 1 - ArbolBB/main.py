from classNodo import *  
from classArbolBB import *  

def insertar_elementos(arbol):
    elementos = [10, 5, 15, 3, 7, 12, 18]
    print("Insertando elementos:", elementos)
    for elemento in elementos:
        arbol.insertar(elemento)

def mostrar_recorridos(arbol):
    print("\nRecorridos del árbol:")
    arbol.preorden()  # Preorden
    arbol.inorden()   # Inorden
    arbol.postorden() # Postorden


def buscar_elemento(arbol, x):
        print(f"\nBuscando el elemento {x}:")
        nodo = arbol.buscar(x)
        print("Elemento encontrado:", nodo.obtener_item())

def calcular_nivel(arbol, x):
        print(f"\nNivel del elemento {x}:")
        nivel = arbol.nivel(x)
        print("Nivel:", nivel)

def verificar_hoja(arbol, x):
    print(f"\n¿El nodo {x} es hoja?", arbol.hoja(x))

def verificar_hijo(arbol, x, z):
    print(f"\n¿El nodo {x} es hijo del nodo {z}?", arbol.hijo(x, z))

def verificar_padre(arbol, x, z):
    print(f"\n¿El nodo {z} es padre del nodo {x}?", arbol.padre(x, z))

def recuperar_camino(arbol, x, z):
        print(f"\nCamino desde {x} hasta {z}:")
        camino = arbol.camino(x, z)
        print("Camino:", ' -> '.join(map(str, camino)))

def calcular_altura(arbol):
    altura = arbol.altura()
    print("\nAltura del árbol:", altura)

def suprimir_elemento(arbol, x):
        print(f"\nSuprimiendo el elemento {x}...")
        arbol.suprimir(x)
        print(f"Elemento {x} suprimido.")

# Ejecutar el programa
if __name__ == "__main__":
    arbol = ABB()

    # Insertar elementos en el árbol
    insertar_elementos(arbol)
    
    # Mostrar recorridos del árbol
    mostrar_recorridos(arbol)

    # Buscar un elemento
    buscar_elemento(arbol, 7)

    # Calcular el nivel de un nodo
    calcular_nivel(arbol, 15)

    # Verificar si un nodo es hoja
    verificar_hoja(arbol, 3)

    # Verificar si X es hijo de Z
    verificar_hijo(arbol, 3, 5)

    # Verificar si Z es padre de X
    verificar_padre(arbol, 5, 10)

    # Recuperar el camino entre dos nodos
    recuperar_camino(arbol, 3, 10)

    # Calcular la altura del árbol
    calcular_altura(arbol)

    # Suprimir un elemento
    suprimir_elemento(arbol, 5)

    # Mostrar recorridos después de la supresión
    mostrar_recorridos(arbol)
