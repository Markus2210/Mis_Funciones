def inicializar_supermercado(cantidad_filas: int, cantidad_columnas: int) -> list:
    return [[0] * cantidad_columnas for _ in range(cantidad_filas)]


def imprimir_supermercado(supermercados):
    for i in range(len(supermercados)):
        print(f"Sucursal {i}: {supermercados[i]}")


def cargar_existencias(supermercados):
    for i in range(len(supermercados)):
        for j in range(len(supermercados[i])):
            cantidad = int(input(f"Ingrese la cantidad de producto {
                           j} para la sucursal {i}: "))
            supermercados[i][j] = cantidad


def cantidad_total_por_sucursal(supermercados):
    for i in range(len(supermercados)):
        total = 0
        for j in range(len(supermercados[i])):
            total += supermercados[i][j]
        print(f"Total en la sucursal {i}: {total}")


def reponer_productos(supermercados):
    for i in range(len(supermercados)):
        productos_a_reponer = []
        for j in range(len(supermercados[i])):
            if supermercados[i][j] < 300:
                productos_a_reponer.append(j)
        if productos_a_reponer:
            print(f"Sucursal {i} necesita reponer productos en las columnas: {
                  productos_a_reponer}")


def maxima_cantidad_por_tipo(supermercados):
    maximos = {}
    for j in range(len(supermercados[0])):
        maximo = 0
        sucursal_maxima = -1
        for i in range(len(supermercados)):
            if supermercados[i][j] > maximo:
                maximo = supermercados[i][j]
                sucursal_maxima = i
        maximos[j] = sucursal_maxima
    print("Máxima cantidad por tipo de producto:", maximos)


def sucursal_con_mayor_valor(supermercados, precios):
    max_valor = 0
    sucursal = -1
    for i in range(len(supermercados)):
        valor = 0
        for j in range(len(supermercados[i])):
            valor += supermercados[i][j] * precios[j]
        if valor > max_valor:
            max_valor = valor
            sucursal = i
    print(f"Sucursal con mayor valor almacenado: {
          sucursal} con un valor de {max_valor}")


def sucursales_mas_20000(supermercados):
    sucursales = []
    for i in range(len(supermercados)):
        total = 0
        for j in range(len(supermercados[i])):
            total += supermercados[i][j]
        if total > 20000:
            sucursales.append(i)
    print("Sucursales con más de 20,000 unidades:", sucursales)


def porcentaje_productos(supermercados):
    total_general = 0
    for i in range(len(supermercados)):
        for j in range(len(supermercados[i])):
            total_general += supermercados[i][j]

    if total_general > 0:
        porcentajes = []
        for i in range(len(supermercados)):
            total_sucursal = 0
            for j in range(len(supermercados[i])):
                total_sucursal += supermercados[i][j]
            porcentaje = (total_sucursal / total_general) * 100
            porcentajes.append(porcentaje)
        print("Porcentaje de productos:", porcentajes)
    else:
        print("No hay productos en el inventario.")


def informe_recaudacion(supermercados, precios):
    recaudaciones = []
    for i in range(len(supermercados)):
        valor = 0
        for j in range(len(supermercados[i])):
            valor += supermercados[i][j] * precios[j]
        recaudaciones.append(valor)

    # Bubble sort para ordenar las sucursales por recaudación
    for i in range(len(recaudaciones)):
        for j in range(0, len(recaudaciones) - i - 1):
            if recaudaciones[j] < recaudaciones[j + 1]:
                recaudaciones[j], recaudaciones[j +
                                                1] = recaudaciones[j + 1], recaudaciones[j]

    print("Sucursales ordenadas por recaudación:", recaudaciones)


def corregir_errores(supermercados):
    for i in range(len(supermercados)):
        for j in range(len(supermercados[i])):
            if supermercados[i][j] < 0:  # Suponiendo que los errores son negativos
                supermercados[i][j] = 500  # Valor predeterminado
    print("Errores corregidos en existencias.")


def menu(supermercados, precios):
    while True:
        print("\nMenú de opciones:")
        print("1. Cargar existencias")
        print("2. Cantidad total por sucursal")
        print("3. Reponer productos")
        print("4. Máxima cantidad por tipo de producto")
        print("5. Sucursal con mayor valor almacenado")
        print("6. Sucursales con más de 20,000 unidades")
        print("7. Porcentaje de productos")
        print("8. Informe de recaudación")
        print("9. Corrección de errores en las existencias")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias(supermercados)
        elif opcion == 2:
            cantidad_total_por_sucursal(supermercados)
        elif opcion == 3:
            reponer_productos(supermercados)
        elif opcion == 4:
            maxima_cantidad_por_tipo(supermercados)
        elif opcion == 5:
            sucursal_con_mayor_valor(supermercados, precios)
        elif opcion == 6:
            sucursales_mas_20000(supermercados)
        elif opcion == 7:
            porcentaje_productos(supermercados)
        elif opcion == 8:
            informe_recaudacion(supermercados, precios)
        elif opcion == 9:
            corregir_errores(supermercados)
        elif opcion == 0:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Inicialización de datos
precios = [10, 20, 30, 40, 50]  # Ejemplo de precios por producto
supermercados = inicializar_supermercado(
    4, 5)  # 4 sucursales y 5 tipos de productos

# Llamar al menú
menu(supermercados, precios)
