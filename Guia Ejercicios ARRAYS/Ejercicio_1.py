# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.


def promedio_lista(lista):
    suma = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            suma += lista[i]
    promedio = suma / len(lista)
    return promedio


lista = [1, 2, 3,  4, 5]
print(promedio_lista(lista))
