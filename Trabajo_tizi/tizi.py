class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        # Función aún no implementada
        pass

    def dividir(self, a, b):
        # Función aún no implementada
        pass


def main():
    calc = Calculadora()
    print("Bienvenido a la Calculadora")

    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar (no disponible)")
        print("4. Dividir (no disponible)")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion in ['1', '2']:
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))

                if opcion == '1':
                    resultado = calc.sumar(a, b)
                    print(f"Resultado: {resultado}")
                elif opcion == '2':
                    resultado = calc.restar(a, b)
                    print(f"Resultado: {resultado}")
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion in ['3', '4']:
            print("Funcionalidad aún no implementada.")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
