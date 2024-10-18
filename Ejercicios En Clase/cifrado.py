# numero = ord('A')  # Convierte una letra en numero
# numero += 13  # desplazamiento

# letra_cifrada = chr(numero)  # convierte numero en letra
# print(letra_cifrada)


mensaje = 'HOLA'
desplazamiento = int(input("Ingrese nro de desplazamiento: "))


def cifrado(mensaje):
    for i in range(len(mensaje, desplazamiento)):
        numero_letra = ord(mensaje[i])
        numero_letra += desplazamiento

    return numero_letra


print(cifrado(mensaje))


def descifrado(mensaje_cifrado, desplazamiento):
    pass
