# Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1  # Condicion de cierre
    else:
        return calcular_potencia(base, exponente - 1)


print(calcular_potencia(2, 4))
