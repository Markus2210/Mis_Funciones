# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron


numero = int(input("Ingrese un numero: "))
es_primo = True
# if numero <= 1 and numero % 2 == 0:
#     print(f"{numero} no es primo")

# else:
#     print(f"{numero} es primo")


for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
