# Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

'''
1
12
123
1234
1235
'''

num = int(input('Ingrese un numero: '))
numeros = ""
for i in range(1, num + 1):
    numeros += str(i)
    print(numeros)
