# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:


# def suma_digitos(numero):
#     suma = 0
#     digitos = numero % 10
#     num = numero - digitos
#     suma += digitos
#     a = num // 10
#     suma += a
#     return suma


# print(suma_digitos(1015))


def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)


numero = int(input('Ingrese un numero: '))

print(suma_digitos(numero))
