import random


def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" | ")
        print("")


def posiconar_barcos(tablero, cant_barcos):
    for i in range(cant_barcos):
        fila = random.randint(0, len(tablero) - 1)
        col = random.randint(0, len(tablero) - 1)
        tablero[fila][col] = 'B'


def batalla(tablero, cant_intentos):
    for i in range(cant_intentos):
        fila = int(input("Ingrese Fila: "))
        Columna = int(input("Ingrese Columna: "))
        if tablero[fila][Columna] == 'B':
            print('HUNDIDO')
            tablero[fila][Columna] = 'X'
        else:
            print('AGUA')
            tablero[fila][Columna] = 'F'


cant_barcos = int(input('Cantidad de barcos: '))
cant_intentos = 5
tablero = inicializar_matriz(5, 5, 0)
posiconar_barcos(tablero, cant_barcos)
imprimir_tablero(tablero)
batalla(tablero, cant_intentos)
imprimir_tablero(tablero)
