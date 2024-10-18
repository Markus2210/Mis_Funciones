# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
num3 = int(input('Ingrese un numero: '))


def maximo(num1, num2, num3):
    max = None
    if num1 > num2 and num1 > num3:
        max = num1
    else:
        if num2 > num1 and num2 > num3:
            max = num2
        else:
            max = num3

    return max


print(f'El numero maximo es {maximo(num1, num2, num3)}')
