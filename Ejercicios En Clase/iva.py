
def calcular_precio_con_iva(valor_sin_iva, iva=21):
    # Documentacion
    resultado = valor_sin_iva * (1 + (iva/100))
    return resultado


# samsung_a32 = 90000 sin iva

precio_sin_iva = 900000

print(f"Samsung A 32 con iva {calcular_precio_con_iva(precio_sin_iva)}")
