"""
UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.

Las posibles aplicaciones son las siguientes:

● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:

● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)

B) Cargar por terminal 10 encuestas.

C) Determinar:

1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.

2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.

3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.

"""

contador = 0
nombre_empleado = None
edad_empleado = None
genero_empleado = None
tecnologia_elegida = None

empleado_mayor_IA = None
edad_maxima_IA = None
tecnologia_elegida_mayor_IA = None

empleado_mayor_RV = None
edad_maxima_RV = None
tecnologia_elegida_mayor_RV = None

empleado_mayor_IOT = None
edad_maxima_IOT = None
tecnologia_elegida_mayor_IOT = None

cant_empleados_IA_IOT = 0
cant_empleados_no_voto_IA = 0

while contador < 10:

    nombre_empleado = input ("Ingrese su nombre aqui: ")

    edad_empleado = int (input ("Ingrese su edad aqui: "))
    while edad_empleado < 18 or edad_empleado > 60:
        edad_empleado = int (input ("Error, edad inválida. Ingrese su edad aqui: "))
    
    genero_empleado = input ("Ingrese su género aqui (M|F|O): ").upper()
    while not (genero_empleado == "M" or genero_empleado == "F" or genero_empleado == "O"):
        genero_empleado = input ("Error, ese genero no se encuentra en las opciónes. Ingrese su género aqui (M|F|O): ").upper()
    
    tecnologia_elegida = input ("Ingrese la tecnología que desea votar ( IA | RV | IOT )").upper()
    while not (tecnologia_elegida == "IA" or tecnologia_elegida == "RV" or tecnologia_elegida == "IOT"):
        tecnologia_elegida = input ("Error, esa tecnología no se puede votar o no existe. Ingrese la tecnología que desea votar ( IA | RV | IOT )").upper()

    match tecnologia_elegida:
        case "IA":
            if empleado_mayor_IA == None or edad_empleado > edad_maxima_IA:
                empleado_mayor_IA = nombre_empleado
                edad_maxima_IA = edad_empleado
        case "RV":
            if empleado_mayor_RV == None or edad_empleado > edad_maxima_RV:
                empleado_mayor_RV = nombre_empleado
                edad_maxima_RV = edad_empleado
        case "IOT":
            if empleado_mayor_IOT == None or edad_empleado > edad_maxima_IOT:
                empleado_mayor_IOT = nombre_empleado
                edad_maxima_IOT = edad_empleado
        
    if genero_empleado == "M" and (edad_empleado <= 50 or edad_empleado >= 25) and (tecnologia_elegida == "IA" or tecnologia_elegida == "IOT"):
        cant_empleados_IA_IOT += 1
    
    if genero_empleado != "F" and (edad_empleado <= 33 or edad_empleado >=40) and tecnologia_elegida != "IA":
        cant_empleados_no_voto_IA +=1

    contador += 1

porcentaje_cant_empleados_no_voto_IA = (cant_empleados_no_voto_IA * 10) / 100

print(f"La cantidad de empleados que votaron IA/IOT masculinos entre 25 y 50 son {cant_empleados_IA_IOT}")
print(f"El porcentaje de empleados que no votaron IA no femeninos y entre 33 y 40 son {porcentaje_cant_empleados_no_voto_IA}%")
print(f"El empleado de IA mayor es {empleado_mayor_IA} de {edad_maxima_IA} de edad")
print(f"El empleado de IA mayor es {empleado_mayor_IOT} de {edad_maxima_IOT} de edad")
print(f"El empleado de IA mayor es {empleado_mayor_RV} de {edad_maxima_RV} de edad")