##range(start, stop, step)

##1
"""
Mostrar los números ascendentes desde el 1 al 10
"""

for i in range(11):
    if i == 0:
        continue
    print(i)

##2
"""
 Mostrar los números descendentes desde el 10 al 1
"""

for i in range (10, 0, -1): ##10 numeros, termina en el 0 y va decrementando de 1 en 1
    print(i)

##3
"""
Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.
"""
numero = int (input("ingrese un numero"))
for i in range(numero):
    print(i)

##4
"""
Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 …
"""

numero = int (input("ingrese un numero"))
for i in range(11):
    print(numero*i)

##5
"""
Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.
"""

suma = 0 
contador = 0

for i in range(10):
    numero = int (input ("Ingrese un número. 0 para finalizar."))
    if numero == 0:
        break
    suma += numero
    contador += 1

promedio = suma / 10

print(f"El total es: {suma} y el promedio es {promedio}")

##6
"""
Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
"""

for i in range(1, 11):
    if i%3 == 0:
        print(i)

##7
"""
Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
"""
for i in range(1, 50):
    if i%2 == 0:
        print(i)

##8
"""
Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente:
1
12
123
1234
12345
"""

cantidad = int (input("Ingrese los peldaños de la pirámide: "))
numeros = ""

for i in range(1, cantidad):
    numeros+=str(i)
    print(numeros)

##9
"""
Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.
"""
numero = int (input ("Ingrese un número: "))

for i in range(1, numero):
    if numero%i == 0:
        print(i)


##10
"""
Ingresar un número. Determinar si el número es primo o no.
"""
numero = int( input("Ingrese un número"))

es_primo = True

if numero<=1:
    es_primo=False

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False

if es_primo: 
    print(f"{numero} es primo")
else:
    print("No es primo") 

##11
"""
Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.
"""
##Defino la función que voy a utilizar:

def es_primo(numero):                   ##Se reutiliza el bucle del ejercicio (10) y se convierte en función
    """
    PROPÓSITO: Indicar si el numero pasado por parámetro es primo o no. 
    PARÁMETRO: Un número
    RETORNA: Bool
    """
    es_primo = True                     #Flag

    if numero<=1:                       #Numeros menores iguales a 1 no son primos, los descarto con el condicional.
        es_primo=False

    for i in range(2, numero):          #Bucle de verificación si el número es primo.
        if numero % i == 0:
            es_primo = False            #Flag = False si el número no es primo. 
    return es_primo

numero = int( input("Ingrese un número: "))

primos = ""                             ##Declaro la variable en la que voy a acumular los números primos en formato string
cantidad_de_primos = 0                  ##Variable para acumular cantidad de primos

for i in range(2, numero + 1):          ##Incluyo el número 5 en la iteración, por eso "número + 1"
    if es_primo(i):                     ##Se parametriza el índice para corroborar si el numero es primo
        primos += "\n" + str(i) + "\n"  ##De ser asi, se añade como string para incluírlo en el prompt - "\n" : line break
        cantidad_de_primos += 1         ##Se incrementa la cantidad pues hay un n° primo.


print(f"En total se encontraron {cantidad_de_primos} de primos, estos son: {primos}")