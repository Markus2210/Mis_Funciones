from .Especificas import *

##Función para mostrar rdos

def print_all(lista) -> list:
    for i in range(len(lista)):
        print(lista[i])

##Función sumatoria (claramente)

def pares(lista):
    listaNueva = []
    for i in range(len(lista)):
        if es_par(lista[i]):
            listaNueva.append(lista[i])
    return listaNueva

def impares(lista):
    listaNueva = []
    for i in range(len(lista)):
        if not es_par(lista[i]):
            listaNueva.append(lista[i])
    return listaNueva

def son_todas_iguales(lista):
    flag = True 
    elemento = lista[0]
    for i in range(len(lista)):
        if elemento != lista[i]:
            flag = False

    return flag

def sum(lista) -> list|int:
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total
##1
def cantidad_postivos(lista) -> list|list:
    cantidad = 0
    for i in range(len(lista)):
        if es_positivo(lista[i]):
            cantidad += 1
    return cantidad

def cantidad_negativos(lista) -> list|list:
    cantidad = 0
    for i in range(len(lista)):
        if not es_par(lista[i]):
            cantidad += 1
    return cantidad 
##2

def sumatoria_pares(lista):
    return sum(pares(lista))

##3 

def mayor_impares(lista):
    return max(impares(lista))

##4

def posiciones_impares(lista):
    posiciones_impares = []
    for i in range(len(lista)):
        if not es_par(i):
            posiciones_impares.append(lista[i])
    return posiciones_impares

##Funcion que me diga que pertenece un elemento

def pertenece(lista,elemento) -> bool:
    flag = False
    for i in range(len(lista)):
        if elemento == lista[i]:
            flag = True
    return flag


    
