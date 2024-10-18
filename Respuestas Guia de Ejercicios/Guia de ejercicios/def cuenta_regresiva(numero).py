def cuenta_regresiva(numero):
    if numero == -1:
        return "Go" 
    else:  
        print(numero)
        return cuenta_regresiva(numero - 1)
    

def calcular_factorial(numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    return resultado

print(calcular_factorial(5))