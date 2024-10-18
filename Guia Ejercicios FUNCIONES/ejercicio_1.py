# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
# area del rectangulo
L1 = int(input('Ingrese el lado de su rectangulo: '))
L2 = int(input('Ingrese el lado de su rectangulo: '))


def area_recangulo(L1, L2):
    area = L1 * L2
    return area


print(area_recangulo(L1, L2))
