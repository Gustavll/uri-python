z = 0
acumulador = 0
for x in range(0,6,1):
    n = float(input(""))
    if n >= 0 :
        z += n
        acumulador += 1
media = z / acumulador
print(f"{acumulador} valores positivos")
print(f"{round(media,1)}")