# Ciclo WHILE

menu_tipo = '\nSELECCIONE TIPO\n\n[1] turismo\n[2] autobus\n[3] motocicleta\n\n\tOPCION: '

contador = 0
turismo = 1700
autobus = 4000
moto = 1000
acum_turismo = 0
acum_autobus = 0
acum_moto = 0

# while contador <= 5:
#     tipo = int(input(menu_tipo))
#     if tipo == 1:
#         acum_turismo += turismo
#     elif tipo == 2:
#         acum_autobus += autobus
#     elif tipo == 3:
#         acum_moto += moto
#     else:
#         print("Vehiculo no autorizado")

#     contador += 1

# print(f"La recaudacion fue de {acum_turismo + acum_autobus + acum_moto}")


# Ciclo for item in range:

for tipo in range(5):
    tipo = int(input(menu_tipo))
    if tipo == 1:
        acum_turismo += turismo
    elif tipo == 2:
        acum_autobus += autobus
    elif tipo == 3:
        acum_moto += moto
    else:
        print("Vehiculo no autorizado")

print(f"La recaudacion fue de {acum_turismo + acum_autobus + acum_moto}")
