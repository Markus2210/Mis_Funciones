'''
UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.
Las posibles aplicaciones son las siguientes:
●Inteligencia artificial (IA),
●Realidad virtual/aumentada (RV/RA),
●Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
●nombre del empleado
●edad (no menor a 18)
●género (Masculino - Femenino - Otro)
●tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.

'''
menu_genero = "\n[GENERO]\nSeleccione genero correpsondiente\n\n[1]Masculino\n\n[2]Femenino\n\n[3]Otro\n\nOpcion: "
menu_tecnologias = "\n[Tecnologias]\nSeleccione la opcion correpsondiente\n\n[1]Inteligencia artificial\n\n[2]Realidad virtual/aumentada\n\n[3]Internet de las cosas\n\nOpcion: "

contador = 0
nombre = None
nombre_max = None
edad = None
edad_max = 0
genero = None
tecnologia = None
tec_voto = None
cant_empleados_masc = 0
cant_no_IA = 0


while contador <= 10:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("[Error].Ingrese su edad: "))

    genero = int(input(menu_genero))
    while genero != 1 and genero != 2 and genero != 3:
        print("[Error]Numero ingresado no válido")
        genero = int(input(menu_genero))

    tecnologia = int(input(menu_tecnologias))
    while tecnologia != 1 and tecnologia != 2 and tecnologia != 3:
        print("[Error]Numero ingresado no válido")
        tecnologia = int(input(menu_tecnologias))

    contador += 1

    if genero == 1:
        if edad == None or edad > edad_max:
            edad_max = edad
            nombre_max = nombre
            tec_voto = tecnologia
        if tecnologia == 1 or tecnologia == 3:
            if edad >= 25 and edad <= 50:
                cant_empleados_masc += 1

    if tecnologia == 2 or tecnologia == 3:
        if genero != 2:
            if edad > 33 and edad < 40:
                cant_no_IA += 1


# Informes
print(f'La cantidad de empleados masculinos que votoaron por IOT o IA es {
      cant_empleados_masc}')
print(f'El porcentaje es de {(cant_no_IA * 100) / contador} ')
print(f'el nombre es {nombre_max} y la tecnologia que voto es {tec_voto}')
