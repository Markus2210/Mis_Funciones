from Package_Input import *
from Package_Arrays import pertenece


def inicializar_matriz(filas, columnas, valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila]

    return matriz


def ingresar_contenido_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)[i]):
            matriz[i][j] = get_int(
                'Ingrese el orden de la matriz:  ', 'Error', -50000, 5000)


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()


def sumatoria_columnas(matriz, orden):

    total = [0] * orden  # Inicializamos una lista de sumas

    # Recorrer la matriz
    for fila in matriz:
        for j in range(orden):
            # Sumar el elemento de la columna i de cada fila
            total[j] += fila[j]

    return total


def sumatoria_columnas(matriz, orden):

    total = [0] * orden  # Inicializamos una lista de sumas

    # Recorrer la matriz
    for fila in matriz:
        for j in range(orden):
            # Sumar el elemento de la columna i de cada fila
            total[j] += fila[j]

    return total


def sumatoria_diagonal(matriz, orden):
    total = 0
    for i in range(orden):
        total += matriz[i][i]
    return total


def verificar_filas(matriz, orden):
    filas = [0] * orden
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz)[i]):
            total += matriz[i][j]
        filas[i] = total
    return son_todos_iguales(filas)


def verificar_columnas(matriz, orden):
    total = [0] * orden
    for fila in matriz:
        for j in range(orden):
            total[j] += fila[j]
        fila[i] = total
    return son_todos_iguales(total)  # solo total suma columnas


def verificar_diagonal(matriz, orden):
    numero = orden*(orden ** 2 + 1) / 2
    return sumatoria_diagonal(matriz) == numero


def son_todos_iguales(lista):  # va en arrays generales

    flag = True
    elemento = lista[0]
    for i in range(len(lista)):
        if elemento != lista[i]:
            flag = False
    return flag
