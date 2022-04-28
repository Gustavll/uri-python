while True:
    n = int(input(""))
    soma = 0
    if n == 0:
        break
    if n % 2 != 0:
        cont = 1
        for i in range(1, 5, 1):
            cont += 2
        for j in range(1, cont + 1, 1):
            if (n + j) % 2 == 0:
                soma += (n + j)
    elif n % 2 == 0:
        cont = 0
        soma = n
        for k in range(1, 5, 1):
            cont += 2
        for l in range(1, cont + 1, 1):
            if (n + l) % 2 == 0:
                soma += (n + l)
    print(soma)