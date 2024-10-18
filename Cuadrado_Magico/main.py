from Package_Arrays import *
from Package_Input import *
from Package_Matrix import *
from Package_Sort import *

# recorrer filas
# recorrer columnas
# recorrer diagonal


def cuadrado_magico():
    orden = get_in('Ingrese orden de matriz', 'Error', -50000, 5000)
    matriz = inicializar_matriz(orden, orden, 0)
    ingresar_contenido_matriz(matriz)

    return verificar_filas(matriz, orden) and verificar_columnas(matriz, orden) and verificar_diagonal(matriz, orden)
