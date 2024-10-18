def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila] 

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
            print(fila)
    print()