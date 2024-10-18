'''
# Desarrollo de una Funcion para Validar Matriculas de Automoviles:
Desarrolla una funcion en Python que valide si una Matricula de automovil cumple con una politica de formato especifica. La funcion debe recibir una matricula como argumento y devolver un valor que indique si la matricula es valida o no, de acuerdo con las reglas establecidas.
'''

matricula = input('Ingrese su matricula [SIN ESPACIOS]: ')


def validacion_matriculas(matricula):

    siete_lugares = False
    numeros = False
    mayusculas = False
    letra = False

    if len(matricula) == 7:
        siete_lugares = True

    for i in range(len(matricula)):
        if matricula[0].isalpha() and matricula[1].isalpha() and matricula[5].isalpha() and matricula[6].isalpha():
            letra = True
        if matricula[2].isdigit() and matricula[3].isdigit() and matricula[4].isdigit():
            numeros = True
        if matricula[i].isupper():
            mayusculas = True

    return siete_lugares and numeros and letra and mayusculas


print(validacion_matriculas(matricula))
