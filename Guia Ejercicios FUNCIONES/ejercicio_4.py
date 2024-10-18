# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

numero = int(input('Ingrese un numero: '))


def num_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(num_par(numero))
