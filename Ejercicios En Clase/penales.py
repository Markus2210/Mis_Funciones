'''
Enunciado:

Escribe un programa que simule la tanda de penales de un equipo de fútbol. El equipo tiene 5 oportunidades para lanzar un penal. Informar el porcentaje de penales fallidos

Instrucciones:

Crea una función para que cada equipo tire su penal. (fallo o gol)
Simula la tanda de penales
Muestra los resultados 

Francia Final 2022

Gol
Fallo
Fallo
Gol
Gol

Porcentaje de Penales Fallidos = Suma_penales_fallidos / total * 100

'''
contador = 1
msj = f'\n[1]Fue Gol\n\n[2]Fallo\n\nOpcion: '
cont_fallo = 0

for i in range(5):
    penal = int(input(f'Penal' + ' ' + f'{contador}{msj}'))
    contador += 1
    if penal == 2:
        cont_fallo += 1


print(f'El porcentaje de fallo es {(cont_fallo / 5)*100}%')
