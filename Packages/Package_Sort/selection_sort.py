def ordenar(lista):
  for i in range(len(lista)):
    minimo = i
    for x in range(i + 1, len(lista)):
      if lista[x] < lista[minimo]:
        minimo = x
    temp = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = temp

  return lista

lista_desordenada = [-4, 7, 2, 78, 90, -1]
print(lista_desordenada)
lista_ordenada = ordenar(lista_desordenada)
print(lista_ordenada)