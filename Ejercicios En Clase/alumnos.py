# En una clase de 5 alumnos se han realizado tres exámenes y se requiere determinar el número de:
# 	Alumnos que aprobaron todos los exámenes
# 	Alumnos que aprobaron por lo menos un examen
# 	Alumnos que aprobaron únicamente el último examen
# A1   N1 N2 N3
# A2   N1 N2 N3
# A3   N1 N2 N3
# A4   N1 N2 N3
# A5   N1 N2 N3

alumno = 1

nota1 = 0
nota2 = 0
nota3 = 0
aprobo_todo = 0
aprobo_una = 0
aprobo_ultimo = 0

while alumno <= 5:
    nota1 = float(input(f"Ingrese la primer nota del alumno {alumno}:  "))
    nota2 = float(input(f"Ingrese la segunda nota del alumno {alumno}:  "))
    nota3 = float(input(f"Ingrese la tercer nota del alumno {alumno}:  "))

    # Aprueba todo
    if nota1 >= 6 and nota2 >= 6 and nota3 >= 6:
        aprobo_todo += 1

    # Aprueba auque sea una
    if nota1 >= 6 or nota2 >= 6 or nota3 >= 6:
        aprobo_una += 1

    # Aprueba solo la ultima
    if nota1 < 6 and nota2 < 6 and nota3 >= 6:
        aprobo_ultimo += 1

    alumno += 1


# Informes
print(f"Los alumnos que aprobaron todos los examenes fueron {aprobo_todo}")
print(f"Los alumnos que aprobaron un examen fueron {aprobo_una}")
print(f"Los alumnos que aprobaron el ultimo examen fueron {aprobo_ultimo}")
