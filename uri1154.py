acum = 0
cont = 0
while True:
    n = int(input(""))
    if n < 0 :
        break
    acum += n
    cont += 1


media = acum / cont
print(f"{media:.2f}")