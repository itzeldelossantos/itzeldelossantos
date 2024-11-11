r = 0
while r < 10:
    valor = float(input("Ingrese un valor: "))
    if valor < 10:
        print("El valor es menor que 10")
    elif 10 <= valor <= 100:
        print("El valor está entre 10 y 100")
    else:
        print("El valor es mayor a 100")
    r += 1
