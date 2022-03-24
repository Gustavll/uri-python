n = int(input(""))
soma = 0
for i in range(0,n,1):
    x,y = input("").split()
    x = int(x)
    y = int(y)
    soma = 0
    if y >= x:
        if x % 2 != 0:
            for j in range(x+1,y,1):
                if j % 2 != 0:
                    soma += j
        if x % 2 == 0:
            for j in range(x,y,1):
                if j % 2 != 0:
                    soma += j
    elif y < x:
        if y % 2 != 0:
            for j in range(y+1,x,1):
                if j % 2 != 0:
                    soma += j
        if y % 2 == 0:
            for j in range(y,x,1):
                if j % 2 != 0:
                    soma += j
    print(soma)