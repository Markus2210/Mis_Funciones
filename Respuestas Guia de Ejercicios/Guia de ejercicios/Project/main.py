from Package_Input.Input import get_int, get_float, get_str

numero_entero = get_int("Ingrese un número entero entre 1 y 10: ", "Número no válido. Intente nuevamente.", 1, 10, 3)
print(f"Número entero ingresado: {numero_entero}")

numero_flotante = get_float("Ingrese un número flotante entre 1.0 y 10.0: ", "Número no válido. Intente nuevamente.", 1.0, 10.0, 3)
print(f"Número flotante ingresado: {numero_flotante}")

cadena = get_str("Ingrese una cadena con 15 caracteres como máximo ", "La cadena no es válida. Debe tener como máximo 15 caracteres.", 15)
print(f"Cadena ingresada: {cadena}")