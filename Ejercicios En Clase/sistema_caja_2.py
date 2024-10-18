comprador = 0
suma = 0
suma_total = 0
iva = 21
msj_producto = f'Ingrese [Y]Para continuar\n\n[Enter]Para salir\t\nOpcion:'

for i in range(6):
    nombre = input("Ingrese su nombre: ")
    concepto = input("Ingrese producto: ")
    if concepto == "":
        break
    precio = int(input("Ingrese precio: "))
    if concepto == "":
        break
    cantidad = int(input("Ingrese cantidad: "))
    if concepto == "":
        break

    suma = precio * 1.21
    suma_total += suma
    msj_renglon = f'\t[Proucto]{concepto}' + ' ' + f'[Precio]${precio}' + ' ' + \
        f'[Cantidad]{cantidad}' + '' + \
        f'[Subtotal]${precio * cantidad}' + \
        f'[IVA]{iva}%'f'[Precio con IVA]{precio * 1.21}'

    print(msj_renglon)
    print('-------------------------------------')
    print(f'Total de compra: {suma_total} ')
    print('-------------------------------------')
