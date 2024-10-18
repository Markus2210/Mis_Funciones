"""
1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
la altura y retorna el área.
"""

def area_rectangulo(base,altura):
    area = base*altura
    return area
#Test
#print(area_rectangulo(4,5))
"""
2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio
como parámetro y devolver el área.
"""
def area_circulo(radio):
    area = 3.14 * radio**2
    return area
#Test
#print(area_circulo(4))
"""
3. Crea una función que verifique si un número dado es par o impar. La función debe
imprimir un mensaje indicando si el número es par o impar.
"""
def es_par_o_impar(numero):
    if numero%2==0:
        return "Es par"
    else:
        return "Es impar"
#Test
#print(es_par_o_impar(5))
"""
4. Crea una función que verifique si un número dado es par o impar. La función retorna
True si el número es par, False en caso contrario.
"""

def es_par(numero):
    return numero%2==0

#Test
#print(es_par(5))
"""
5. Define una función que encuentre el máximo de tres números. La función debe
aceptar tres argumentos y devolver el número más grande.
"""

def max_3(n1,n2,n3):
    return max(n1,n2,n3)

#Test
#print(max_3(4,9,15725))
"""
6. Diseña una función que calcule la potencia de un número. La función debe recibir la
base y el exponente como argumentos y devolver el resultado.
"""

def potencia(numero,exponente):
    return numero**exponente

#Test
#print(potencia(11,2))

"""
7. Crear una función que reciba un número y retorne True si el número es primo, False
en caso contrario.
"""

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

#Test
#print(es_primo(5))

"""
8. Crear una función que (utilizando la función del punto 11 de la guía de For), muestre
todos los números primos comprendidos entre entre la unidad y un número
ingresado como parámetro. La función retorna la cantidad de números primos
encontrados.
"""
def todos_los_primos(numero):
                           
    cantidad_de_primos = 0                  

    for i in range(2, numero + 1):          
        if es_primo(i):                     
            cantidad_de_primos += 1         
    return cantidad_de_primos

#Test
#print(todos_los_primos(7))
"""
9. Crear una función que imprima la tabla de multiplicar de un número recibido como
parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
el rango de multiplicación. Por defecto es del 1 al 10.
"""

def tabla_multiplicar(numero):
    for i in range(1,11):
       print(i*numero) 

#Test
#print(tabla_multiplicar(2))

"""
10. Crear una función que le solicite al usuario el ingreso de un número entero y lo
retorne.
"""
def get_entero():
    numero = int(input("Ingrese un número entero"))
    return numero

#Test
#print(get_entero())

"""
11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
retorne.
"""
def get_flotante():
    numero = float(input("Ingrese un número flotante"))
    return numero
"""
12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
"""
def get_cadena():
    string = str(input("Ingrese una cadena de texto"))
    while string == "" and string.isalpha():
        string = str(input("Ingrese una cadena de texto"))
    return string

cadena = get_cadena()
print(cadena)
"""
13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
validaciones.
"""