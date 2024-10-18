from Package_Input import get_int, get_float, get_string

if __name__ == "__main__":
    numero_entero = get_int("Ingrese un número entero entre 1 y 10: ", "Número no válido. Intente nuevamente.", 1, 10, 3)
    print(f"Número entero ingresado: {numero_entero}")

    numero_flotante = get_float("Ingrese un número flotante entre 1.0 y 10.0: ", "Número no válido. Intente nuevamente.", 1.0, 10.0, 3)
    print(f"Número flotante ingresado: {numero_flotante}")

    cadena = get_string("Ingrese una cadena de texto entre 3 y 10 caracteres: ", "La cadena no es válida. Debe tener entre 3 y 10 caracteres.", 3, 10, 3)
    print(f"Cadena ingresada: {cadena}")