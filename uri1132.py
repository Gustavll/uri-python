x = int(input(""))
y = int(input(""))
soma = 0
if x >= y :
    for i in range(y,x+1,1):
        if i % 13 != 0:
            soma += i
elif x < y :
    for j in range(x,y+1,1):
        if j % 13 != 0:
            soma += j
print(soma)
