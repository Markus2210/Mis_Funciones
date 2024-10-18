# Calculadora simple
# El usuario va a ingresar el operador y los operarios
# Ejemplo:
#          + 2 3  -> 5
#          * 7 3  -> 21
# Termina cuando el usuario ingresa "F" (Finalizar)

# Funciones

def sumar(operador1, operador2):
    # Documentacion
    rdo = operador1 + operador2
    return rdo


def restar(operador1, operador2):
    # Documentacion
    rdo = operador1 - operador2
    return rdo


def multiplicar(operador1, operador2):
    # Documentacion
    rdo = operador1 * operador2
    return rdo


def dividir(operador1, operador2):
    # Documentacion
    rdo = operador1 / operador2
    return rdo

# Procesamiento principal


menu = 'SELECCIONE OPERADOR\n\n [+] Suma\n\n[-] Resta\n\n[*] Multiplicacion\n\n[/] Division\n\n[F] Finalizar\n\n\tOPCION: '
resultado = 0

while (True):
    operador = input(menu)
    while operador != "+" and operador != "-" and operador != "*" and operador != "/" and operador != "F":
        print('[ERROR] INGRESO NO VALIDO!!!')
        operador = input(menu)

    if operador == "F":
        break

    operario1 = float(input('Ingrese el primer numero: '))
    operario2 = float(input('Ingrese el segundo numero: '))

    if operador == "+":
        resultado = operario1 + operario2
    else:
        if operador == "-":
            resultado = operario1 - operario2
        if operador == "*":
            resultado = operario1 * operario2
        else:
            resultado = operario1 / operario2

    print(f"El resultado es {resultado}")
