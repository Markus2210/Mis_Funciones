'''
Sistema de Reserva de Butacas de Cine

Desarrolla un programa en Python que simule un sistema de reserva de butacas en una sala de cine. El cine tiene una disposición de asientos en una matriz de tamaño 5x5, donde cada celda representa una butaca.

Requisitos del Sistema:

Visualización del Cine:

El programa debe mostrar el estado actual de las butacas, donde:
'O' representa una butaca disponible.
'X' representa una butaca ocupada.
Al inicio, todas las butacas están disponibles.

Reserva de Asientos:

El usuario puede reservar una butaca proporcionando el número de fila y de columna.
Si la butaca está disponible, se marca como ocupada y se muestra un mensaje de confirmación.
Si la butaca ya está ocupada, se muestra un mensaje indicando que no está disponible y se le pide que seleccione otra.

Cancelar una Reserva:

El usuario puede cancelar la reserva de una butaca, proporcionando su fila y columna.
Si la butaca está ocupada, se marca como disponible nuevamente y se muestra un mensaje de confirmación.
Si la butaca no está ocupada, se indica que no hay una reserva en esa posición.

Salir del Sistema:

El sistema debe permitir al usuario realizar varias reservas o cancelaciones, hasta que decida salir.
'''


def inicializar_sala(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


def imprimir_sala(butacas):
    for i in range(len(butacas)):
        for j in range(len(butacas[i])):
            print(butacas[i][j], end=" | ")
        print("")


def reserva_asiento(butacas, cant_entradas):
    for i in range(cant_entradas):
        fila = int(input("Ingrese Fila: "))
        Columna = int(input("Ingrese Columna: "))
        while butacas[fila][Columna] != 0:
            print('Butaca ocupada')
            fila = int(input("Ingrese Fila: "))
            Columna = int(input("Ingrese Columna: "))
        else:
            print("Reserva exitosa")
            butacas[fila][Columna] = 'X'


def cancelar_entrada(butacas, cant_entradas):
    for i in range(cant_entradas):
        fila = int(input("Ingrese Fila: "))
        Columna = int(input("Ingrese Columna: "))
        while butacas[fila][Columna] != 'X':
            print('No hay una reserva en esa posición')
            fila = int(input("Ingrese Fila: "))
            Columna = int(input("Ingrese Columna: "))
        else:
            print('Cancelacion Exitosa')
            butacas[fila][Columna] = '0'


butacas = inicializar_sala(5, 5, 0)
msj_menu = 'SELECCIONE UNA OPCION\n\n[1]Visualización del Cine\n[2]Reserva de Asientos\n[3]Cancelar una Reserva\n[4]Salir del Sistema\n\n\tOPCION: '


while True:
    menu = int(input(msj_menu))

    match menu:
        case 1:
            imprimir_sala(butacas)
        case 2:
            cant_entradas = int(input('Cantidad de entradas: '))
            reserva_asiento(butacas, cant_entradas)
            imprimir_sala(butacas)
        case 3:
            cant_entradas = int(input('Cantidad de entradas: '))
            cancelar_entrada(butacas, cant_entradas)
            imprimir_sala(butacas)
        case 4:
            break
