def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


mi_matriz = inicializar_matriz(2, 4, 8)


def carga_matriz_secuencialmente(matriz: list):
    # Agregar las validaciones/retonro que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))


carga_matriz_secuencialmente(mi_matriz)
