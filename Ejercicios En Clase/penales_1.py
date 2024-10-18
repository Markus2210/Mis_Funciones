'''
Realizar un funcion...los resultados de los penales.

Va a devolver la cantidad de penales convertidos y errados
Van a cargar dos tandas de penales de dos equipos
Informar quien gano
Caso 1:

1. gol
2. falla
3. glo
4. falla
5. gol
'''


def carga_penales():

    msj = f'\n[1]Fue Gol\n\n[2]Fallo\n\nOpcion: '
    contador = 1
    cont_fallo = 0
    cont_gol = 0
    # cuerpo de la funcion
    for i in range(5):
        penal = int(input(f'Penal' + ' ' + f'{contador}{msj}'))
        contador += 1
        if penal == 2:
            cont_fallo += 1
        else:
            cont_gol += 1

    convertidos = cont_gol
    fallados = cont_fallo
    return convertidos, fallados


def ganador():
    print("Primer Equipo")
    conv, erra = carga_penales()
    print("Segundo Equipo")
    conv2, erra2 = carga_penales()

    if conv > conv2:
        return (f"Gano el equipo 1 con {conv} penales convertidos y {erra} penales fallados")
    else:
        return (f"Gano el equipo 2 con {conv2} penales convertidos y {erra2} penales fallados")


print(ganador())
