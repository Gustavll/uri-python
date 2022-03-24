x = 1
acumulador = 0
while x <= 6:
    n = float(input(""))
    if n >= 0 :
        acumulador +=1
    x += 1
print(f"{acumulador} valores positivos")