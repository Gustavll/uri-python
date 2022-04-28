import random


def soma(x):
    print(x)
    soma = 0
    for i in range(len(x)):
        soma += x[i]
    print(f"{soma:.1f}")
    return


def media(x):
    print(x)
    soma = 0
    for i in range(len(x)):
        soma += x[i]
    media = soma / len(x)
    print(f"{media:.1f}")
    return


def main():
    linha = int(input(""))
    operacao = input("")
    matriz = []
    for i in range(0,12):
        linhaAux = []
        for j in range(0,12):
            #numero = float(input())
            numero = random.randint(0, 99)
            linhaAux.append(numero)
        matriz.append(linhaAux)
    if operacao == 's':
        soma(matriz[linha])
    elif operacao == 'm':
        media(matriz[linha])
    for l in range(0, 12):
        for k in range(0, 12):
            print(f"[{matriz[l][k]:^5}]", end=" ")
        print()


main()