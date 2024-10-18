# Ingresar un número. Determinar si el número es primo o no.
num = int(input('Ingrese un numero: '))

if num <= 1 or num % 2 == 0:
    print(f"{num} no es primo")
else:
    print(f"{num} es primo")
