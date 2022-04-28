def avaliador():
    par = []
    impar = []
    p = 0
    i = 0
    for j in range(0,15):
        x = int(input(""))
        if x % 2 == 0:
            par.append(x)
            p += 1
        elif x % 2 != 0:
            impar.append(x)
            i += 1
        if p == 5:
            impressãopar(par)
            par.clear()
            p = 0
        if i == 5:
            impressãoimpar(impar)
            impar.clear()
            i = 0
    impressãoimpar(impar)
    impressãopar(par)


def impressãopar(par):
    if len(par) == 5:
        for k in range(0,5):
            print(f"par[{k}] = {par[k]}")
    else:
        for l in range(0,len(par)):
            print(f"par[{l}] = {par[l]}")


def impressãoimpar(impar):
    if len(impar) == 5:
        for j in range(0, 5):
            print(f"impar[{j}] = {impar[j]}")
    else:
        for l in range(0,len(impar)):
            print(f"impar[{l}] = {impar[l]}")


def main():
    avaliador()


main()

'''1
3
4
-4
2
3
8
2
5
-7
54
76
789
23
98'''