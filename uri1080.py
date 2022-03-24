'''l = []  # inicia a lista L
for i in range(0,100,1):  # inicia um loop de 0 a 99 com passo 1
    n = int(input(""))  # recebe um valor n do tipo inteiro
    l.append(n)  # adciona o valor n no final da lista l
l_max = max(l)  # ultiliza a função max para identificar o valor maximo da lista e armazenar na variavel l_max
l_pos = l.index(l_max)  # ultiliza a função index para identificar a posição da variavel l_max na lista e armazena na
# variavel l_pos
print(l_max)  # mostra na tela valor maximo
print(l_pos)  # mostra na tela o index do valor maximo'''

x=0  # inicia uma variavel com valor 0

for i in range(1,100,1):  # inicia um loop de 1 a 100 com passo 1
    a = int(input()) # recebe um valor a do tipo inteiro
    if a > x:  # avalia se a for maior que x
        maior = a  # então maior recebe o valor de a
        posicao = i + 1  # e posição recebe o valor de i + 1
        x = a  # o x recebe o valor de a, e está pronto para a nova sequencia.

print(maior)   # ao final imprime o valor de maior e o valor de posição
print(posicao)