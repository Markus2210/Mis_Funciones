def quick_sort(list):
    min = []        ##init lista menores a pivote                ##NOMBRAR VARIABLES FELICES
    max = []        ##init lista mayores a pivote   
    if len(list) <=1:
        return list ##Caso borde recursividad, lista de un solo elemento
    else: 
        pivote = list[0]
            ##Tomo el primer elemento como pivote(segun ppt puede ser primero,ultimo o random)
        for x in range(1,len(list)):    ##Itero la lista sin el pivote
            if list[x] <= pivote:
                min += [list[x]]     ## if int < 1 = > list min
            else:
                max += [list[x]]     ##otherwise
    return quick_sort(min) + [pivote] + quick_sort(max)     ##Se vuelve a hacer el mismo proceso sobre los max
            ##se vuelve a hacer el mismo proceso sobre los min

            ##se concatenan las tres listas: min (ya ordenados) + pivote + max (ya ordenados)

lista = [33,10,59,270,1,90,50]
print(lista)
print(quick_sort(lista))
    