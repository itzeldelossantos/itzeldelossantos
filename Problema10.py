r = 0
while r < 24:
    apellido = input("Ingrese el apellido del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del examen: "))
    print(f"{apellido} {nombre} - Nota: {nota}")
    r += 1
