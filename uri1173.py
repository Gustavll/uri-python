x = int(input(""))
n = []
n.append(x)
proximo = x
for i in range(0,10):
    proximo = proximo * 2
    n.append(proximo)
    print(f"N[{i}] = {n[i]}")