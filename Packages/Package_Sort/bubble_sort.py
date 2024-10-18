def ordenar_burbuja(lista):
    for i in range(len(lista)):
        for x in range(0, len(lista) - i - 1):
            if lista[x] > lista[x + 1]:
                temp = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = temp
    return lista

lista_desordenada = [4, 7, 2, 78, 90, -1]
print(lista_desordenada)
lista_ordenada = ordenar_burbuja(lista_desordenada)
print(lista_ordenada)

## [2,-1,1,-3]
##