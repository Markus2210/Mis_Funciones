# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
# Consideraciones : no voy a dejar que ingrese una cadena vacia

def get_string():
    cadena = input("mensaje")
    while cadena == "":
        cadena = input("mensaje")
    return cadena
