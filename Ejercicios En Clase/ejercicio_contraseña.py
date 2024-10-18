'''
Desarrollo de una Funcion para Validar Politicas de Contraseñas:

Desarrola una funcion en Python que valide si una contraseña cumple con una politica de seguridad espécifica. La funcion debe recibir una contraseña como argumento y devolver un valor que indique si la contraseña cumple o no con las politicas definidas.

# La contraseña debe cumplir con:
# Tener al menos 8 caracteres
# Contener al menos una letra mayuscula
# Contener al menos una letra minuscula
# Contener al menos un numero

caracter.isalpha() #Si es un caracter alfabetico
caracter.isdigit() #Si es un digito
caracter.isupper() #Si es mayusculas
caracter.islower() #Si es minusculas
'''

contra = input('Ingrese su contraseña: ')


def validacion(contra):

    Ocho_digitos = False
    mayusculas = False
    minusculas = False
    numeros = False
    alpha = False

    if len(contra) >= 8:
        Ocho_digitos = True

    for i in range(len(contra)):
        if contra[i].isdigit():
            numeros = True
        if contra[i].isalpha():
            alpha = True
        if contra[i].isupper():
            mayusculas = True
        if contra[i].islower():
            minusculas = True

    return Ocho_digitos and mayusculas and minusculas and numeros and alpha


print(validacion(contra))
