sueldo = int(input("Ingrese el sueldo del empleado: "))
años_trabajo = int(input("Ingrese los años trabajados: "))
if años_trabajo < 5:
    antiguedad = sueldo * 0.3
else:
    antiguedad = sueldo * 0.5
sueldo_total = sueldo + antiguedad
print("El sueldo a cobrar es:", sueldo_total)
