#  Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
lista = [1, 2, 10, 4, 10]


def maximo(lista):
    max = 0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max


def posiciones_valor_max(lista) -> list:
    lista1 = []

    for i in range(len(lista)):
        if lista[i] == maximo(lista):
            lista1.append(i)
    return lista1


print(posiciones_valor_max([2, 4, 3, 1, 4, 0, 1, 3, 4, 2, 4]))
