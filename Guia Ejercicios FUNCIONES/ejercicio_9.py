#  Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales(inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
numero = int(input('Ingrese un numero: '))


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(i*numero)


print(tabla_multiplicar(numero))
