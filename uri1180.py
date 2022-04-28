def menor(x):
    menor = x[0]
    posicao = 0
    posicaoAtual = 0
    for i in x:
        if i < menor:
            menor = i
            posicaoAtual = posicao
        posicao += 1
    print(f"Menor valor: {menor}")
    print(f"Posicao: {posicaoAtual}")


def main():
    n = int(input(""))
    x = map(int, input("").split())
    x = list(x)
    menor(x)


main()