def sumatoria_filas(colectivos):
    filas = []
    for i in range(len(colectivos)):
        total = 0
        for j in range(len(colectivos[i])):
            total += colectivos[i][j]
        filas += [total]  # Concatenamos la lista
    return filas


def sumatoria_filas(colectivos):
    filas = []
    for i in colectivos:
        filas.append(sum(i))
    return filas


def sumatoria_columnas(colectivos):
    suma = []
    for i in range(len(colectivos)):
        suma_columna = 0
        for j in range(len(colectivos[i])):
            suma_columna += colectivos[i][j]

        suma.append(suma_columna)
    return suma
