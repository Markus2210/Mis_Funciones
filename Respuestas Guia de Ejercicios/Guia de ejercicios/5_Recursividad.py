##1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero:int)->int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)
           
print(sumar_naturales(5))

##2. Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base:int,exponente:int)->int:
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente - 1)

##3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero: int)-> int:
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos (numero//10)
                #Me da el resto                 #me da el número
                #de dividir el                  #redondeado para abajo
                #número por 10

##4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

def calcular_fibonacci(numero:int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else: 
        return calcular_fibonacci(numero - 2) + calcular_fibonacci(numero - 1)

