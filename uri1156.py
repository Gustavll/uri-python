'''s = 1
x = 2
y = 3
z = 2
while True:
    s += y/x
    print(f"{y}/{x}")
    if y == 39:
        break
    x = x + z
    z += 2
    y += 2

print(f"{s:.2f}")'''
s=0
j = 1
for i in range(1,40,2):
    s = float(s + i / j)
    j = j * 2
print('{:.2f}'.format(s))