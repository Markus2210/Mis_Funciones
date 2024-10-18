# Programa de gestión de estudiantes y notas

def main():
    # Ingreso de datos
    num_estudiantes = int(
        input("Ingrese la cantidad de estudiantes a registrar: "))

    nombres = []
    edades = []
    notas = []

    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
        nota = float(input(f"Ingrese la nota final del estudiante {i + 1}: "))

        nombres.append(nombre)
        edades.append(edad)
        notas.append(nota)

    # Mostrar información
    print("\nLista de estudiantes:")
    for i in range(num_estudiantes):
        print(
            f"Nombre: {nombres[i]}, Edad: {edades[i]}, Nota final: {notas[i]}")

    # Cálculo de promedio
    promedio = sum(notas) / num_estudiantes
    print(f"\nEl promedio de las notas finales es: {promedio:.2f}")

    # Buscar estudiante
    nombre_busqueda = input("\nIngrese el nombre del estudiante a buscar: ")
    if nombre_busqueda in nombres:
        index = nombres.index(nombre_busqueda)
        print(f"Edad: {edades[index]}, Nota final: {notas[index]}")
    else:
        print("Estudiante no encontrado.")

    # Estudiante con mayor nota
    if notas:
        mayor_nota_index = notas.index(max(notas))
        print(
            f"\nEl estudiante con la mayor nota es: {nombres[mayor_nota_index]} con una nota de {notas[mayor_nota_index]}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
