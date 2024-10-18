''' funcion potencia(base, exponente)
pero sin utilizar el operador de potencia ** (Prohibido)
multiplicaciones sucesivas
'''


def potencia_de_numero(base, exponente):
    potencia = 1
    for i in range(1, exponente + 1):
        potencia *= base

        return potencia

    print(potencia_de_numero(2, 3))


def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1  # Condicion de cierre
    else:
        return calcular_potencia(base, exponente - 1)


print(potencia_de_numero(2, 4))
print(calcular_potencia(2, 4))
