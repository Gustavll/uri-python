def preenchimento(x):
    n = []
    for i in range(0,100):
        if i == 0:
            n.append(x)
            print(f"N[{i}] = {n[i]:.4f}")
        else:
            x = x / 2
            n.append(x)
            print(f"N[{i}] = {n[i]:.4f}")


def main():
    x = float(input(""))
    preenchimento(x)


main()
