x = int(input(""))
y = int(input(""))
soma = 0
if x >= y :
    for i in range(y+1,x,1):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
elif x < y :
    for j in range(x+1,y,1):
        if j % 5 == 2 or j % 5 == 3:
            print(j)