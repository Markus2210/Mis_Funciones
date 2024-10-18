MENSAJE_INICIAL = "Hola, bienvenidos a Programacion I"
MESNAJE_FINAL = "Gracias por asistir"


def saludar(mensaje: str) -> None:
    print(mensaje)


def saludar_alumno(nombre: str, mensaje: str) -> None:
    print(f"Hola, {nombre}. {mensaje}")


def saludar_profesor(nombre: str, materia: str) -> None:
    print(f"Hola,soy el profe{nombre}de la materia {materia}")
