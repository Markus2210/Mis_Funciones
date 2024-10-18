def inicializar_matriz(filas, columnas):
    return [['O' for _ in range(columnas)] for _ in range(filas)]


def imprimir_tablero(butacas):
    for fila in butacas:
        print(' '.join(fila))


def reservar_asiento(butacas, fila, columna):
    if 0 <= fila < len(butacas) and 0 <= columna < len(butacas[0]):
        if butacas[fila][columna] == 'O':
            butacas[fila][columna] = 'X'
            print("Asiento reservado correctamente.")
        else:
            print("Asiento ya ocupado.")
    else:
        print("Coordenadas inválidas.")


def cancelar_reserva(butacas, fila, columna):
    if 0 <= fila < len(butacas) and 0 <= columna < len(butacas[0]):
        if butacas[fila][columna] == 'X':
            butacas[fila][columna] = 'O'
            print("Reserva cancelada correctamente.")
        else:
            print("Asiento no reservado.")
    else:
        print("Coordenadas inválidas.")

# ... Resto del código con las llamadas a las funciones y el menú ...


while True:
    # ... Menú y opciones ...
    match menu:
        case 1:
            imprimir_tablero(butacas)
        case 2:
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))
            reservar_asiento(butacas, fila, columna)
        # ... Resto de los casos ...
