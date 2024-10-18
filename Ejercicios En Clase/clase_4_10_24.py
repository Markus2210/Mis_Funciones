def quicksort(vector):
    if len(vector) < 1:  # Si es 0 o 1
        return vector
    else:
        pivote = vector[0]

        vector_izq = []
        vector_der = []

        for i in range(1, len(vector)):
            if vector[i] <= pivote:
                vector_izq += [vector[i]]
            else:
                vector_der += [vector[i]]

    return quicksort(vector_izq) + [pivote] + quicksort(vector_der)


lista = [9, -3, 5, 2, 6, 8, -6, 1, 3]
lista_ordenada = quicksort(lista)

print(lista_ordenada)
