from classArbolB import *

class Main:
    def __init__(self):
        self.__btree = BTree(n=2)  # Definir el orden del árbol B (n = 2 en este caso)

    def iniciar(self):
        while True:
            op = int(input("\nMenú:\n1. Insertar\n2. Suprimir\n3. Mostrar\n4. Salir\nIngrese opción: "))
            if op == 1:
                x = int(input("Ingrese clave a insertar: "))
                self.__btree.insertar(x)
            elif op == 2:
                x = int(input("Ingrese clave a suprimir: "))
                self.__btree.suprimir(x)
            elif op == 3:
                self.__btree.mostrar()
            elif op == 4:
                break

# Ejecución principal
if __name__ == "__main__":
    main_program = Main()
    main_program.iniciar()
