n = int(input(""))
k = []
x = 0
y = 1
z = 0
if n == 1:
    k.append(x)
elif n == 2:
    k.append(x)
    k.append(y)
else:
    k.append(x)
    k.append(y)
    for i in range(0,n):
        z = x + y
        k.append(z)
        x = y
        y = z
print(*k[:n])