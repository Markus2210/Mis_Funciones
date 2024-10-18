# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

numero = int(input('Ingrese un numero: '))


def es_primo(numero):
    es_primo = True
    if numero <= 1:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

    return es_primo


print(es_primo(numero))
