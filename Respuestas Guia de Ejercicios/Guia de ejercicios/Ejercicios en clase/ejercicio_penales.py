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
'''
    def porcentaje_tanda():
        total_disparos = 0 
        for i in range(5):
            user_input = str (input ("Jugador dispara: GOL | FALLO ")).upper()
            disparo = esFallo(user_input)
            total_disparos += disparo
        return porcentaje_de_fallos(total_disparos)    

    def esFallo(disparo):
        if disparo == "FALLO":
            return 1
        else:
            return 0 

    def porcentaje_de_fallos(total):
        porcentaje_de_fallos = total / 5 * 100
        return porcentaje_de_fallos

    print(porcentaje_tanda())
'''

def carga_penales():
    convertidos = 0 
    fallados = 0
    for i in range(5):
        user_input = str (input ("Jugador dispara: GOL | FALLO ")).upper()
        if es_gol(user_input):
            convertidos += 1
        else:
            fallados += 1 
    return convertidos, fallados   

def es_gol(disparo):
        if disparo == "GOL":
            return True
        else:
            return False

def definir_ganador():
    print("Cargue los penales del primer equipo")
    conv1, erra1 = carga_penales()
    print("Cargue los penales del segundo equipo") 
    conv2, erra2 = carga_penales()

    if conv1 > conv2:
        return (f"Ganó el primer equipo por {conv1} a {conv2}. El equipo ganador erro {erra1} y el perdedor {erra2}")
    elif conv2 > conv1:
        return (f"Ganó el segundo equipo, por {conv2} a {conv1}. El equipo ganador erro {erra2} y el perdedor {erra1}")
    else:
        return (f"Ambos equipos empataron con la misma cantidad de convertidos {conv1} y fallados {erra1}")
    
print(definir_ganador())