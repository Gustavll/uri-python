l = int(input(""))
for i in range(0,l):
    n = int(input(""))
    k = []
    x = 0
    y = 1
    z = 0
    if n == 1:
        k.append(x)
        k.append(y)
    elif n == 2:
        k.append(x)
        k.append(y)
        k.append(1)
    else:
        k.append(x)
        k.append(y)
        for p in range(0, n):
            z = x + y
            k.append(z)
            x = y
            y = z
    print(f'Fib({n}) = {k[n]}')