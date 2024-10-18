import random


# <------------------------------------- MENÚ --------------------------------------------- >


# mensaje_menu = "Seleccione la opción: \n\n[1] para ... \n[2] para ... \n[3] para ...\n"
# mensaje_menu += "[4] para ... \n[5] para... \n[6] para ... \n"
# mensaje_menu += "[7] para ... \n[8] para... \n\nSELECCIONE: "

# while True:
#     menu = int(input(mensaje_menu))

#     match menu:
#         case 1:
#             pass
#         case 2:
#             pass
#         case 3:
#             pass
#         case 4:
#             pass
#         case 5:
#             pass
#         case 6:
#             pass
#         case 7:
#             pass
#         case 8:
#             break


# <------------------------------------- MATRICES ------------------------------------------>


# Inicializar matríz
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:

    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


# CARGAR matriz SECUENCIALMENTE
def cargar_matriz_secuencialmente(matriz: list):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f" Fila: {i} Columna {j}:  "))


# CARGAR matriz ALEATORIAMENTE
def cargar_matriz_aleatoriamente(matriz: list):

    seguir = "S"
    while seguir == "S":
        #        fila = get_int("Ingrese índice de fila: ", "Error. Intente nuevamente", minimo:int, maximo:int, reintentos:int)
        #        columna = get_int("Ingrese índice de columna: ", "Error. Intente nuevamente", minimo:int, maximo:int, reintentos:int)
        dato = int(input("Ingrese el dato para guardar en matríz: "))
#        matriz[fila][columna] = dato
        seguir = input(
            "Desea seguir cargando datos? S para continuar/ N para salir: ")


# Cargar aleatoriamente con función RANDINT
def cargar_aleatorios(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            dato = random.randint()
            matriz[i][j] = dato

    return matriz


# IMPRIMIR Matriz
def imprimir_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")
        print(" ")


# BUSCAR dato en matriz
def buscar_valor_entero(matriz: list, valor: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz == valor:
                print(f"Se encontró el dato en fila {i} columna {j} !")


# Ordenar una lista de números enteros: Desarrollar una función que ordene una lista de números enteros
# recibiendo como parámetro el criterio de ordenamiento "ASC" o "DESC" (ascendente o descendente).
# aclaración: Está hecha con bubble sort
def ordenar_matriz(lista, orientacion="ASC"):

    if orientacion == "ASC":
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
        return lista
    else:
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
        return lista


# Suma absolutamente TODOS los elementos de la matriz
def sumatoria_total(matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]
    return total


# Suma todos los elementos de la FILA
def sumatoria_fila(matriz: list):
    suma_total_filas = []
    for i in range(len(matriz)):
        sumatoria_elementos = 0
        for j in range(len(matriz[i])):
            sumatoria_elementos += matriz[i][j]
        suma_total_filas += [sumatoria_elementos]
    return suma_total_filas


# Suma todos los elementos de la COLUMNA
def sumatoria_columna(matriz: list):
    suma_total_columna = []

    for j in range(len(matriz)):
        sumatoria_elementos = 0
        for i in range(len(matriz)):
            sumatoria_elementos += matriz[i][j]
        suma_total_columna += [sumatoria_elementos]
    return suma_total_columna


# Verifica igualdad en la suma total de elementos de cada fila y retorna booleano
def verificar_igualdad_suma_de_filas(matriz: list) -> bool:

    for i in range(len(matriz)):
        if matriz[i] != matriz[0]:
            return False
    return True


# Verifica igualdad en la suma total de elementos de cada COLUMNA y retorna booleano
def verificar_igualdad_suma_de_columnas(matriz: list) -> bool:

    for j in range(len(matriz)):
        if matriz[j] != matriz[0]:
            return False
    return True


# Verifica si el cuadrado es mágico (si tanto filas como columnas son iguales)
def es_cuadrado(matriz: list, matriz_dos: list) -> bool:
    if matriz and matriz_dos == True:
        return True
    else:
        return False


###
def lista_string(lista):
    string = ""
    for i in range(len(lista)):
        string += lista[i]
    return string


# Verificar número repetido en matriz
def verificar_numero_repetido_en_matriz(matriz: list, numero: int) -> bool:

    bandera_numero_repetido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido


# Validar si la lista existe
def validar_lista(lista):
    return lista != []


# Validar si la lista existe
def validar_lista_existente(lista):
    if validar_lista(lista):
        return True
    else:
        print("Error, antes de realizar esta acción tiene que iniciar la lista (elegir la opción 1)")
        return False


# Verifica rangos de una lista
def rango(rango_inferior, rango_superior, lista, mensaje_error):
    lista_nueva = []
    for i in range(len(lista)):
        if rango_inferior <= lista[i] <= rango_superior:
            lista_nueva += [lista[i]]
    if validar_lista(lista_nueva):
        return lista_nueva
    else:
        return mensaje_error


# Devuelve el valor máximo de la lista
def valor_max(lista):
    max = float("-inf")

    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max


# Devuelve el valor mínimo de la lista
def valor_min(lista):
    min = float("inf")

    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min


# Genera lista de datos aleatorios agregados con RANDINT
def lista_aleatorios():

    lista = [0] * 123232323

    for i in range(len(lista)):
        lista[i] = random.randint(1, 100)
    return lista


# Dice que pertenece un dato
def verificar_existencia_de_dato(lista, dato, mensaje) -> bool:
    bandera = False
    for i in range(len(lista)):
        if dato == lista[i]:
            bandera = True
    if not bandera:
        print(mensaje)
    return bandera


#  <------------------------------------ GET Y VALIDATES ------------------------------------------->


def validate_number(number, min, max):
    try:
        if min <= number <= max:
            return number

    except ValueError:
        return None


def validate_lenght(str, lenght):
    try:
        if len(str) <= lenght:
            return str

    except ValueError:
        return None


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int):

    for _ in range(reintentos):
        user_input = int(input(mensaje))
        numero = validate_number(user_input, minimo, maximo)
        if numero is not None:
            return numero
        else:
            print(mensaje_error)
    return None


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int):

    for _ in range(reintentos):
        user_input = float(input(mensaje))
        numero = validate_number(user_input, minimo, maximo)
        if numero is not None:
            return numero
        else:
            print(mensaje_error)
    return None


def get_str(mensaje: str, mensaje_error: str, longitud: int) -> str | None:
    user_input = str(input(mensaje))
    string = validate_lenght(user_input, longitud)
    if string is not None:
        return string
    else:
        print(mensaje_error)

    return None


# TRUE sería (dato = alphabetic, dato = numeric, dato = alnumeric)
def validar_ingreso_alfnum(dato):
    return verificar_numero(dato) and verificar_alfabetico(dato)


# Verifica si el dato es numérico
def verificar_numero(dato):
    bandera = False
    for i in range(len(dato)):
        if dato[i].isnumeric():
            bandera = True
    return bandera


# Verifica si el dato es alfabético
def verificar_alfabetico(dato):
    bandera = False
    for i in range(len(dato)):
        if dato[i].isalpha():
            bandera = True
    return bandera


def ordenar_burbuja(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista
