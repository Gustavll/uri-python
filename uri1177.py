def preenchimento(t):
    n = []
    k = 0
    for j in range(0,1000):
        if k < t:
            n.append(k)
        if k == t:
            k = 0
            n.append(k)
        k += 1
        print(f"N[{j}] = {n[j]}")


def main():
    t = int(input(""))
    preenchimento(t)


main()