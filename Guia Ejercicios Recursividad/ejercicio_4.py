#  Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_fibonacci(numero - 2) + calcular_fibonacci(numero - 1)


print(calcular_fibonacci(9))
