# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
contador = 0
suma_numero = 0
cont_promedio = 0

for i in range(11):
    contador += 1
    msj = f"Ingrese numero {contador}\n[Con 0 finaliza]: "
    numero = int(input(msj))
    if numero == 0:
        break
    suma_numero += numero
    cont_promedio += 1

print(f"La suma es {suma_numero}")
print(f"El promedio es {(suma_numero / cont_promedio)}")
