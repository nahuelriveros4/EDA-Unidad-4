from classArbolHuffman import *

def calcular_frecuencias(texto):
        frecuencias = {}
        for caracter in texto:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        return frecuencias

def comprimir(texto, codigos):
        texto_comprimido = ""
        for caracter in texto:
            texto_comprimido += codigos[caracter]
        return texto_comprimido


def main ():
    with open("Ejercicio 3/archivo.txt", "r") as archivo:
        texto = archivo.read() 

    frecuencias = calcular_frecuencias(texto)

    arbol_huffman = ArbolHuffman()
    arbol_huffman.construir_arbol(frecuencias)

    codigos_huffman =  arbol_huffman.generar_codigos()

    texto_comprimido = comprimir(texto, codigos_huffman)
    
    with open("Ejercicio 3/archivo_comprimido.txt", "w") as archivo_comprimido:
        archivo_comprimido.write(texto_comprimido)

    print("Códigos de Huffman generados:", codigos_huffman)
    print("Texto comprimido guardado en 'archivo_comprimido.txt'")

if __name__ == "__main__":
    main()
