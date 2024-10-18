# Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return numero + sumar_naturales(numero - 1)


print(sumar_naturales(5))
