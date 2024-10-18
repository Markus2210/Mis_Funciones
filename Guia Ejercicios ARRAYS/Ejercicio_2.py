# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

lista = [-1, -2, 3, 4, 5]


def promedio(lista):
    suma = 0
    num_post = 0

    for i in range(len(lista)):

        if lista[i] > 0:
            suma += lista[i]
            num_post += 1 
    promedio_len = num_post / len(lista)

    return promedio_len


print(promedio(lista))
