# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
'''
radio = 4
area_circulo = 3.14 * radio ** 2
'''

radio = int(input('Ingrese el radio de su circulo: '))


def area_circulo(radio):
    area = 3.14 * radio ** 2
    return area


print(area_circulo(radio))
