# def burbuja(lista):
#     while True:
#         flag = False
#         for i in range(len(lista) - 1):
#             if lista[i] > lista[i + 1]:
#                 auxiliar = lista[i]
#                 lista[i] = lista[i + 1]
#                 lista[i + 1] = auxiliar
#                 flag = True

#         if flag == False:
#             break

#     return lista


# lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]
# lista_ordenada = burbuja(lista)
# print(lista_ordenada)


#  Recorro la lista
# Si el elemento 0 es menor que el elemento 1,queda igual,sino se invierte


def selection(lista):
    for i in range(0, len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j

        auxiliar = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = auxiliar

    return lista


lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]
lista_ordenada = selection(lista)
print(lista_ordenada)


# Recorre la lista
# Encuentra el mas chico y lo pone en primer lugar
# Encuentea el segundo mas chico y lo pone en segundo lugar
