vetor = []  # inicia uma lista com nome vetor
while True:  # inicia um loop infinito enquanto verdade
    m, n = input("").split()   # recebe dois valores na mesma linha ultilizando split
    m = int(m)  # converte de string para inteiro
    n = int(n)  # converte de string para inteiro
    if m <= 0 or n <= 0:  # se m ou n forem menores que 0 então o loop acaba ultilizando break
        break
    if m >= n:  # se m é maior ou igual a n
        vetor.extend(range(n, m))  # então o vetor vai ser preenchido com valores entre n e m(porém sem contar com o m
        vetor.append(m)  # como o extend não conta com o m, ultilizando append o valor m é adcionado ao final do vetor
    elif m < n:  # se o m é menor que o n
        vetor.extend(range(m, n))  # então o vetor vai ser preenchido com valores entre m e n (porém sem contar com o n)
        vetor.append(n)  # como o extend não conta com o n, ultilizando append o valor n é adcionado ao final do vetor
    vetorsum = sum(vetor)  # ultilizando a função sum para somar os valores do vetor e guardando na variavel vetorsum
    print(*vetor, "Sum={}".format(vetorsum))  # imprime somente o conteudo do vetor ultilizando o * e depois imprime
    # a variavel vetor sum
    vetor = []  # limpa o vetor para mais um loop
