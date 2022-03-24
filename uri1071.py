n1 = int(input(""))
n2 = int(input(""))
soma = 0
if n1 > n2:
    for i in range(n2,n1+1,1):
        if i != n2 and i != n1:
            if i % 2 != 0:
                soma += i
elif n2 > n1:
    for i in range(n1-1,n2,1):
        if i != n2 and i != n1:
            if i % 2 != 0:
                soma += i
print(f'{soma}')