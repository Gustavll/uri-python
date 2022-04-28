def soma(x):
    som = 0
    for i in range(len(x)):
        som += x[i]
    print(f"{som:.1f}")
    return


def media(x):
    som = 0
    for i in range(len(x)):
        som += x[i]
    medi = som / len(x)
    print(f"{medi:.1f}")
    return


def main():
    linha = int(input(""))
    operacao = input("")
    matriz = []
    for i in range(0,12):
        linhaAux = []
        for j in range(0,12):
            numero = float(input())
            linhaAux.append(numero)
        matriz.append(linhaAux)
    if operacao == 'S':
        soma(matriz[linha])
    elif operacao == 'M':
        media(matriz[linha])


main()