from Package_Input import *
from Package_Arrays import son_todas_iguales,pertenece

def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila] 

    return matriz

def ingresar_contenido_matriz(matriz):
    for i in range(len(matriz)):
         for j in range(len(matriz[i])):
              matriz[i][j] = get_int("Ingrese un valor numerico: ","Error",-50000,50000,50000) 

def imprimir_matriz(matriz):
    for fila in matriz:
            print(fila) 
    print()


## RESOLUCIÓN EJERCICIO

def sumatoria_filas(matriz,orden):
    filas = [0] * orden
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total += matriz[i][j]
        filas[i] = total
    return total

def sumatoria_columnas(matriz, orden):

    total = [0] * orden  # Inicializamos una lista de sumas

    # Recorrer la matriz
    for fila in matriz:
        for j in range(orden):
            total[j] += fila[j]  # Sumar el elemento de la columna i de cada fila

    return total

def sumatoria_diagonal(matriz,orden):
    total = 0

    for i in range(orden):
        total += matriz[i][i]
    
    return total

def verificar_filas(matriz,orden):
    filas = [0] * orden
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total += matriz[i][j]
        filas[i] = total
    return son_todas_iguales(filas)

def verificar_columnas(matriz, orden):

    total = [0] * orden  # Inicializamos una lista de sumas

    # Recorrer la matriz
    for fila in matriz:
        for j in range(orden):
            total[j] += fila[j]  # Sumar el elemento de la columna i de cada fila

    return son_todas_iguales(total)


def verificar_diagonal(matriz,orden):
    '''
    flag = False
    
    if verificar_columnas(matriz, orden) and verificar_columnas(matriz, orden):
        flag = pertenece(sumatoria_columnas(matriz,orden),sumatoria_diagonal(matriz,orden))
    '''
    numero = orden * (orden**2 + 1 ) / 2 

    return sumatoria_diagonal(matriz,orden) == numero



## Inicializo la lista filas=[0,0]
## Va al for 1
## inicializa la sumatoria (total=0)
## Va al for 2
    ##Desde el for 2 y ya parado en la fila actual, realiza la sumatoria y el rdo está en total
    ##Termina el for 2
##Vuelvo al for 1
##le asigno al primer elemento de la lista "filas" el rdo de la sumatoria
##quedaría filas = [sumatoria,0]

##Recien ahí voy a i + 1 

## inicializa la sumatoria (total=0)
## Va al for 2
    ##Desde el for 2 y ya parado en la fila actual, realiza la sumatoria y el rdo está en total
    ##Termina el for 2
##Vuelvo al for 1
##le asigno al primer elemento de la lista "filas" el rdo de la sumatoria
##quedaría filas = [sumatoria,sumatoria2]



