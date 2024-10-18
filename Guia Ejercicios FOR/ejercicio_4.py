'''
Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 …
'''

numero = int(input("Ingresar un numero: "))

msj = '\n\n'
msj += '[Tabla del (numero)]\n\n'
msj += f"\t{numero} x 0 = {(numero) * 0}\n\n"
msj += f"\t{numero} x 1 =  {(numero) * 1}\n\n"
msj += f"\t{numero} x 2 =  {(numero) * 2}\n\n"
msj += f"\t{numero} x 3 =  {(numero) * 3}\n\n"
msj += f"\t{numero} x 4 =  {(numero) * 4}\n\n"
msj += f"\t{numero} x 5 =  {(numero) * 5}\n\n"
msj += f"\t{numero} x 6 =  {(numero) * 6}\n\n"
msj += f"\t{numero} x 7 =  {(numero) * 7}\n\n"
msj += f"\t{numero} x 8 =  {(numero) * 8}\n\n"
msj += f"\t{numero} x 9 =  {(numero) * 9}\n\n"
msj += f"\t{numero} x 10 =  {(numero) * 10}\n\n"


for i in range(11):
    print(msj)
