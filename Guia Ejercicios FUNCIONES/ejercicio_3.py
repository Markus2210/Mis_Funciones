# 3. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

numero = int(input('Ingrese un numero: '))


def num_par(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"


print(num_par(numero))
