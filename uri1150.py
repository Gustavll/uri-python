x = int(input(""))
z = int(input(""))
acumulador = x
contador = 1
while z <= x:
    z = int(input(""))
for i in range(x,z,1):
    acumulador += (x + contador)
    if acumulador > z:
        contador += 1
        break
    contador += 1
print(contador)