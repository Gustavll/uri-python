n = int(input(""))
for i in range(0, n, 1):
    soma = 0
    a, b = input("").split()
    a = int(a)
    b = int(b)
    if a % 2 != 0:
        cont = 0
        soma = a
        for l in range(1, b, 1):
            cont += 2
        for j in range(1, cont + 1, 1):
            if (a + j) % 2 != 0:
                soma += (a + j)
    elif a % 2 == 0:
        cont = 1
        for r in range(1, b, 1):
            cont += 2
        for k in range(1, cont + 1, 1):
            if (a + k) % 2 != 0:
                soma += (a + k)
    print(soma)
