'''
Sistema de Caja Simple
Solicitar al usuario
Nombre:
Numerar la factura(Sistema)
Solicitar cada renglon de la factura
Concepto (procudto)
Cantidad

Condicion de corte cuando el usuario ingresa Concepto = " "

Imprimir el Total de la Factura

'''
n_factura = 1
suma = 0
suma_total = 0
iva = 21
msj_producto = f'Ingrese [Y]Para continuar\n\n[Enter]Para salir\t\nOpcion:'


nombre = input("Ingrese su nombre: ")
print(f'Bienvenido' + ' ' +
      f'{nombre}.[Recuerde que cuando quiera salir presione enter en cualquier opcion]')
while (True):
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

# msj_boleta = f'\t[Proucto]{concepto}' + ' ' + f'[Precio]${precio}' + ' ' + \
#     f'[Cantidad]{cantidad}' + '' + \
#     f'[Subtotal]${precio * cantidad}' + \
#     f'[IVA]{iva}%'f'[Precio con IVA]{precio * 1.21}'

# print(msj_boleta)
print(f'Total de compra: {suma_total} ')
