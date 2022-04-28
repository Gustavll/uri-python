x = []
for i in range(0,10,1):
    n = int(input(""))
    x.append(n)
    if n <= 0:
        x.pop()
        x.append(1)
    print(f"x[{i}] = {x[i]}")