def cuenta_regresiva(numero):
    if numero == -1:
        return numero
    else:
        print(numero)
        return cuenta_regresiva(numero - 1)


cuenta_regresiva(10)
