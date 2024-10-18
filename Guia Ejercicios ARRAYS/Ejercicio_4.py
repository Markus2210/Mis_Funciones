#  Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

lista = [1, 2, 10, 4, 5]


def posicion_del_elemento(lista):
    max = 0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
    return lista.index(max)


print(posicion_del_elemento(lista))
