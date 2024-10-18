'''
Ejercicio: Gestión de Estudiantes y Notas

En una universidad, se desea gestionar la información de un grupo de estudiantes. Para ello, se te pide desarrollar un programa en Python que utilice arrays paralelos para almacenar la siguiente información de cada estudiante:

Nombre del estudiante
Edad del estudiante
Nota final del estudiante

El programa debe realizar las siguientes tareas:

Ingreso de Datos: Solicitar al usuario que ingrese la cantidad de estudiantes que va a registrar y luego ingresar para cada uno:
*Nombre
*Edad
*Nota final
Mostrar Información: Imprimir por pantalla la lista de estudiantes con su respectiva edad y nota final.
Cálculo de Promedio: Calcular e imprimir el promedio de las notas finales de todos los estudiantes.
Buscar Estudiante: Permitir al usuario ingresar el nombre de un estudiante y mostrar su edad y nota final. Si el estudiante no existe, mostrar un mensaje apropiado.
Estudiante con Mayor Nota: Mostrar el nombre del estudiante con la mayor nota.

Menú
====
1. Ingresar Datos
2. Mostrar Información
3. Calculo del Promedio
4. Busqueda de Estudiantes
5. Estudiante con Mayor Nota
6. Salir
Ingrese la opción: 1
'''


def ingreso_datos(nombre_lista, edad_lista, notas_lista, cant_estudiantes):

    for i in range(cant_estudiantes):

        nombre = input('Ingrese el nombre: ')
        nombre_lista[i] = nombre
        legajo = input('Ingrese su legajo: ')
        legajo_lista[i] = legajo
        edad = int((input('Ingrese su edad: ')))
        edad_lista[i] = edad
        nota_final = int(input('Ingrese la nota final: '))
        notas_lista[i] = nota_final


def mostrar_lista(nombre_lista, edad_lista, notas_lista):

    for i in range(len(nombre_lista)):
        print(
            f"Legajo: {legajo_lista[i]} Nombre: {nombre_lista[i]} Edad: {edad_lista[i]} Nota Final: {notas_lista[i]}")


def promedio(notas_lista):
    suma = 0
    for i in range(len(notas_lista)):
        if notas_lista[i] > 0:
            suma += notas_lista[i]
    promedio = suma / len(notas_lista)


def buscar_estudiante(nombre_lista):
    nombre_buscar = input('Ingrese el nombre que dese buscar: ')
    for i in range(nombre_lista):
        if nombre_lista[i] == nombre_buscar:
            nombre_buscar = nombre_lista[i]
            print(
                f"Nombre: {nombre_lista[i]}, Edad: {edad_lista[i]}, Nota Final: {notas_lista[i]}")


def maximo(notas_lista):
    max = 0
    for i in range(len(notas_lista)):
        if notas_lista[i] > max:
            max = notas_lista[i]
            print(
                f"El alumno con mayor nota es: {nombre_lista[i]}")


cant_estudiantes = int(input('Ingrese la cantidad de estudiantes: '))
nombre_lista = [0] * cant_estudiantes
edad_lista = [0] * cant_estudiantes
notas_lista = [0] * cant_estudiantes
legajo_lista = [0] * cant_estudiantes


msj_menu = 'SELECCIONE UNA OPCION\n\n[1]Ingresar datos\n[2]Mostar Información\n[3]Calculo del Promedio\n[4]Busqueda de Estudiantes\n[3]Estudiant con mayor nota\n\n[6] SALIR\n\n\tOPCION: '

while True:
    menu = int(input(msj_menu))

    match menu:
        case 1:
            ingreso_datos(nombre_lista, edad_lista,
                          notas_lista, cant_estudiantes)
        case 2:
            mostrar_lista(nombre_lista, edad_lista, notas_lista)
        case 3:
            promedio(notas_lista)
        case 4:
            buscar_estudiante(nombre_lista)
        case 5:
            maximo(notas_lista)
        case 6:
            break
