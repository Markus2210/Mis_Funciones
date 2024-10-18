# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

base = int(input('Ingrese su numero base: '))
exponente = int(input('Ingrese su exponente: '))


def potencia(base, exponente):
    resultado = base ** exponente
    return resultado


print(potencia(base, exponente))
