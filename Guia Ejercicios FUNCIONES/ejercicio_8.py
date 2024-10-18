#  Crear una función que(utilizando la función del punto 11 de la guía de For), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados.
numero = int(input('Ingrese un numero: '))


def es_primo(numero):
    es_primo = True
    if numero <= 1:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

    return es_primo


def cantidad_primos(numero):
    cant_primos = 0

    for i in range(numero):
        if es_primo(i):
            cant_primos += 1

    return cant_primos


print(cantidad_primos(numero + 1))
