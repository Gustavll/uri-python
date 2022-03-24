acp = 0
aci = 0
acpo = 0
acne = 0
for x in range(0,5,1):
    n = int(input(""))
    if n > 0:
        acpo += 1
        if n % 2 == 0:
            acp += 1
        else:
            aci += 1
    elif n < 0:
        acne += 1
        if n % 2 == 0:
            acp += 1
        else:
            aci += 1
    else:
        if n % 2 == 0:
            acp += 1
        else:
            aci += 1

print(f"{acp} valor(es) par(es)\n{aci} valor(es) impar(es)\n{acpo} valor(es) positivo(s)\n{acne} valor(es) negativo(s)")