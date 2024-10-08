from classNodoHuffman import *

class ArbolHuffman:
    __raiz = object
    def __init__(self):
        self.__raiz = None

    
    def construir_arbol(self, frecuencias):
        lista_nodos = []
        for caracter, frecuencia in frecuencias.items():
            nodo = Nodo(caracter, frecuencia)
            lista_nodos.append(nodo)
        while len(lista_nodos) > 1:
            lista_nodos.sort(key=lambda nodo: nodo.get_frecuencia())
            nodo1 = lista_nodos.pop(0)
            nodo2 = lista_nodos.pop(0)
            nuevo_nodo= Nodo(None, nodo1.get_frecuencia() + nodo2.get_frecuencia())
            nuevo_nodo.set_izq(nodo1)
            nuevo_nodo.set_der(nodo2)
            lista_nodos.append(nuevo_nodo)
        self.__raiz = lista_nodos[0]
        
    def generar_codigos_recursivo(self, nodo, codigo_actual, codigos):
        if nodo is None:
            return
        if nodo.es_hoja():
            codigos[nodo.get_caracter()] = codigo_actual
        self.generar_codigos_recursivo(nodo.get_izq(), codigo_actual + "0", codigos)
        self.generar_codigos_recursivo(nodo.get_der(), codigo_actual + "1", codigos)

    def generar_codigos(self):
        codigos = {}
        self.generar_codigos_recursivo(self.__raiz, "", codigos)
        return codigos

    

    

