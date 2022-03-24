acumulador = 0
for x in range(0,5,1):
    if x != 0:
        n = int(input(""))
        print(x)
        if n % 2 == 0 :
            acumulador += 1
print(f"{acumulador} valores pares")
