n = int(input(""))
for i in range(0,n):
    soma = 0
    valor = int(input(""))
    for j in range(2,valor,1):
        if valor % j == 0:
            soma += 1
    if soma == 0:
        print(f"{valor} eh primo")
    else:
        print(f"{valor} nao eh primo")