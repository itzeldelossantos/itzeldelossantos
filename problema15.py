cont_menora10 = 0
cont_10a100 = 0
cont_mayorque100 = 0
cont_negativo = 0
cont_cero = 0

for _ in range(100):
    valor = float(input("Ingrese un valor: "))
    if valor > 0 and valor < 10:
        cont_menora10 += 1
    elif 10 <= valor <= 100:
        cont_10a100 += 1
    elif valor > 100:
        cont_mayorque100 += 1
    elif valor < 0:
        cont_negativo += 1
    else:
        cont_cero += 1

print("Mayor a 0 y menor a 10:", cont_menora10)
print("Entre 10 y 100:", cont_10a100)
print("Mayor a 100:", cont_mayorque100)
print("Negativo:", cont_negativo)
print("Igual a 0:", cont_cero)
