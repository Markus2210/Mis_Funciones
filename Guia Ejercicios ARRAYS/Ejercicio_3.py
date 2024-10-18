# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

lista = [2, 2, 2, 2]


def producto(lista):
    mult = 0

    for i in range(len(lista)):
        mult *= lista[i]

    return mult


print(producto(lista))
