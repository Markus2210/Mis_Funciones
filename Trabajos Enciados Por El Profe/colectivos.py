

def inicializar_legajos(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    contador = 1
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        for j in range(cantidad_columnas):
            fila[j] = contador
            contador += 1

        matriz += [fila]

    return matriz


def imprimir_legajos(legajos):
    for i in range(len(legajos)):
        for j in range(len(legajos[i])):
            # legajos[i][j] = random.randint(1, 16)
            print(legajos[i][j], end=" | ")
        print("")


def inicializar_colectivos(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


def imprimir_colectivos(colectivos):
    for i in range(len(colectivos)):
        for j in range(len(colectivos[i])):
            print(colectivos[i][j], end=" | ")
        print("")


# def legajo_choferes(legajos):
#     for i in range(len(legajos)):
#         for j in range(len(legajos[i])):
#             legajos[i][j] = random.randint(1, 16)


def validacion_legajo(legajos):
    while True:
        chofer = int(input('Ingrese su legajo: '))
        flag = False

        for i in range(len(legajos)):
            for j in range(len(legajos[i])):
                if legajos[i][j] == chofer:
                    print('Legajo CORRECTO')
                    flag = True

        if flag:
            break
        else:
            print('Legajo INEXISTENTE. Intente nuevamente.')
            chofer = int(input('Ingrese su legajo: '))


def carga_recaudacion(colectivos, cant_recaudacion):
    for i in range(cant_recaudacion):
        fila = int(input("Ingrese Fila: "))
        Columna = int(input("Ingrese Columna: "))
        monto_recaudado = int(input('Ingrese el monto recaudado: '))
        colectivos[fila][Columna] = monto_recaudado


def imprimir_fila(fila):
    for i in range(len(fila)):
        print(fila[i])


def imprimir_columna(columna):
    for i in range(len(columna)):
        print(columna[i])


def sumatoria_filas(colectivos):
    filas = []
    for i in range(len(colectivos)):
        total = 0
        for j in range(len(colectivos[i])):
            total += colectivos[i][j]
        filas += [total]
    return filas


def sumatoria_columnas(colectivos):
    total = [0] * len(colectivos[0])  # Inicializamos una lista de sumas

    # Recorrer la matriz
    for fila in colectivos:
        for j in range(len(colectivos)):
            # Sumar el elemento de la columna i de cada fila
            total[j] += fila[j]

    return total


def recaudacion_total(colectivos):
    suma = 0
    suma_total = []
    for i in range(len(colectivos)):
        for j in range(len(colectivos)):
            suma += colectivos[i][j]
    suma_total += [suma]
    print(suma_total)


legajos = inicializar_legajos(3, 5, 0)
print("=====LEGAJOS=====")
imprimir_legajos(legajos)
print("=====COLECTIVOS=====")
colectivos = inicializar_colectivos(3, 5, 0)
imprimir_colectivos(colectivos)
columna = ["\tCOLUMNAS", "(0)Coche 1", "(1)Coche 2", "(2)Coche 3",
           "(3)Coche 5", "(4)Coche 4"]
fila = ["\n\tFILAS", "(0)Linea 1", "(1)Linea 2",
        "(2)Linea 3"]


msj_menu = 'SELECCIONE UNA OPCION\n\n[1]Cargar planilla\n[2]Mostrar la recaudación de cada coche y línea\n[3]Calcular y mostrar recaudación por línea\n[4]Calcular y mostrar recaudación por coche\n[5]Calcular y mostrar la recaudación total\n[6]Salir del Sistema\n\n\tOPCION: '

while True:
    menu = int(input(msj_menu))

    match menu:
        case 1:
            validacion_legajo(legajos)
            cant_recaudacion = int(
                input('Ingrese cuantas recaudaciones quiere cargar: '))
            imprimir_fila(fila)
            imprimir_columna(columna)
            carga_recaudacion(colectivos, cant_recaudacion)
        case 2:
            imprimir_colectivos(colectivos)
        case 3:
            print(sumatoria_filas(colectivos))
        case 4:
            print(sumatoria_columnas(colectivos))
        case 5:
            recaudacion_total(colectivos)
        case 6:
            break
