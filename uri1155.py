s = 1
x = 2
while True:
    s += 1/x
    if x == 100:
        break
    x += 1
print(f"{s:.2f}")