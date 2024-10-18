import random


def inicializar_legajos(cantidad_filas: int, cantidad_columnas: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [random.randint(1, 15) for _ in range(cantidad_columnas)]
        matriz.append(fila)
    return matriz


legajos = inicializar_legajos(3, 5)
print(legajos)
