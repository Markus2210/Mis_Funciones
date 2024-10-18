from Package_Matrix import verificar_filas,ingresar_contenido_matriz,inicializar_matriz,verificar_columnas,verificar_diagonal 
from Package_Input import * 

##Recorrer filas
##Recorrer columnas         ##la suma de c/u tiene que ser el mismo n°
##Recorrer diagonal          

def es_cuadrado_magico():


    orden = get_int("Ingrese el orden de la matriz: ", "Error, el númeoro debe ser mayor a 2", 3,5,100)

    matriz = inicializar_matriz(orden,orden,0)

    ingresar_contenido_matriz(matriz) 

    return verificar_filas(matriz,orden) and verificar_columnas(matriz,orden) and verificar_diagonal(matriz,orden)

print(es_cuadrado_magico())

'''
    [8, 1, 6]
    [3, 5, 7]
    [4, 9, 2]

    son_todas_iguales([15,15,15])

    M = n*(n2 + 1)/2

        un cuadrado mágico de orden n, es
una matriz cuadrada de nxn donde los números
enteros del 1 al n2
'''