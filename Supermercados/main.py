'''
ENUNCIADO
Una cadena de supermercados posee 4 sucursales distribuidas en diferentes provincias(Santa Fe, Córdoba, Buenos Aires, y Salta). Cada sucursal puede almacenar 5 tipos diferentes de productos: frutas, verduras, carnes, bebidas, y lácteos.
Cada mes, la oficina central recibe un informe con las existencias de cada producto en cada sucursal. El objetivo es implementar un programa con un menú de opciones para gestionar y analizar estas existencias.
Menú de opciones:
1. Cargar existencias: El programa deberá cargar las existencias de cada tipo de producto en cada sucursal. Almacenará estos datos en una matriz, donde cada fila representa una sucursal y cada columna un tipo de producto.
2. Cantidad total por sucursal: Calcular la cantidad total de productos almacenados en cada sucursal sumando todas las categorías.
3. Reponer productos: Crear una función que devuelva los productos que tienen menos de 300 unidades en cada sucursal y que, por lo tanto, necesitan ser repuestos.
4. Máxima cantidad por tipo de producto: Crear una función que devuelva la provincia que almacena la mayor cantidad de cada tipo de producto(frutas, verduras, etc.).
5. Sucursal con mayor valor almacenado: Cada producto tiene un precio por unidad. Se dispone de una lista con los precios de cada tipo de producto. Crear una función que determine qué sucursal tiene el mayor valor económico almacenado. La función debe recibir la lista de precios por parámetro.
6. Sucursales con más de 20.000 unidades: Crear una función que devuelva las sucursales que tienen más de 20.000 unidades almacenadas entre todos los productos.
7. Porcentaje de productos: Crear una función que calcule el porcentaje de cada tipo de producto respecto al total de productos almacenados en todas las sucursales.
8. Informe de recaudación: ** Crear una función que ordene las sucursales según la recaudación total(cantidad de productos por su valor) usando el algoritmo de ordenamiento bubble sort o selection sort. Justificar la elección del algoritmo.
9. Corrección de errores en las existencias: Crear una función que permita corregir un error de carga en la matriz de existencias mediante la generación aleatoria o distribución equitativa de las cantidades.
'''


def imprimir_fila(fila):
    for i in range(len(fila)):
        print(fila[i])


def imprimir_columna(columna):
    for i in range(len(columna)):
        print(columna[i])


def inicializar_supermercado(cantidad_filas: int, cantidad_columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


def imprimir_super(supermercados):
    for i in range(len(supermercados)):
        for j in range(len(supermercados[i])):
            print(supermercados[i][j], end=" | ")
        print("")


def carga_existencias(supermercados, cant_carga):
    for i in range(cant_carga):
        fila = int(input("Ingrese Fila: "))
        Columna = int(input("Ingrese Columna: "))
        Cantidad = float(input("Ingrese la cantidad: "))
        supermercados[fila][Columna] = Cantidad


def total_productos(supermercados):
    total = []
    for i in range(len(supermercados)):
        total += supermercados[i]
    return total


def reponer_producto(supermercados):
    super_reponer = []
    for i in range(len(supermercados)):
        mercado = []
        for j in range(len(supermercados[i])):
            if supermercados[i] < 300:
                mercado += supermercados[i]


supermercados = inicializar_supermercado(4, 5, 0)
columna = ["\tCOLUMNAS", "(0)Frutas", "(1)Verduras", "(2)Carnes",
           "(3)Bebidas", "(4)Lácteos"]


fila = ["\n\tFILAS", "(0)Santa Fe", "(1)Córdoba",
        "(2)Buenos Aires", "(3)Salta"]
# imprimir_super(supermercados)
# carga_existencias(supermercados)


menu = 'SELECCIONE UNA OPCION\n\n[1]Cargar existencias\n[2]Cantidad total por sucursal\n[3]Reponer productos\n[4]Máxima cantidad por tipo de product\n[5]Sucursal con mayor valor almacenados\n[6]Sucursales con más de 20.000 unidades\n[7]Porcentaje de productos\n[8]Informe de recaudación\n[9]Corrección de errores en las existencias\n[0]Salir del Sistema\n\n\tOPCION: '
menu_mercados = 'SELECCIONE UNA OPCION\n\n[1]Santa Fe\n[2]Córdoba\n[4]Buenos Aires\n[5]Salta\n\n OPCION: '
menu_carga = 'SELECCIONE CUANTO TIPO PRODUCTOS DESEA CARGAR: '

while True:
    menu = int(input(menu))

    match menu:
        case 1:
            cant_carga = int(input(menu_carga))
            imprimir_fila(fila)
            imprimir_columna(columna)
            carga_existencias(supermercados, cant_carga)
            print("CARGA EXITOSA")
            imprimir_super(supermercados)
        case 2:
            total_productos(supermercados)
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case _:
            break

            #             cant_entradas = int(input('Cantidad de entradas: '))
            #             reserva_asiento(butacas, cant_entradas)
            #             imprimir_sala(butacas)
            #         case 3:
            #             cancelar_entrada(butacas, cant_entradas)
            #             imprimir_sala(butacas)
            #         case 4:
            #             break
