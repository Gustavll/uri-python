'''nota_soma = 0
cont = 0
continuar = True

while continuar == True:
    nota = float(input())

    if nota >= 0.0 and nota <= 10:
        nota_soma += nota
        cont += 1

        if cont == 2:

            print("media = %.2f" % (nota_soma / 2))
            cont = 0
            nota_soma = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                novo = int(input())
                if novo == 2:
                    continuar = False
                    break
                elif novo == 1:
                    continuar = True
                    break

    else:
        print("nota invalida")'''
r = 0  # inicia a variavel r com o valor 0
i = 0  # inicia a variavel i com o valor 0
media = 0  # inicia a variavel media com o valor 0
c = '1'  # inicia a variavel c com a string '1'
while c == '1':  # enquanto c tiver o valor '1' o loop deve continuar
    r = 0  # a variavel r é reiniciada(em caso do laço ser refeito)
    nota = float(input())  # recebe o valor da nota na variavel nota
    if 0 <= nota <= 10:  # se a nota estiver entre 0 e 10
        i += 1  # então o i acrescenta 1
        media += nota  # a variavel media acrescenta a nota atual ao seu valor
    if nota < 0 or nota > 10:  # se a nota estiver abaixo de zero ou a cima de 10
        print('nota invalida')  # imprime nota invalida na tela
        nota = 0  # a nota é zerada recebendo o valor 0
    if i == 2:  # se a variavel i tiver o valor igual a 2, significa que duas notas validas já foram armazenadas
        media /= 2  # então é efetuado o calculo da media
        print(f"media = {media:.2f}")  # é imprimido o valor final da media com duas casas decimais
        print("novo calculo (1-sim 2-nao)")  # é imprimido na tela a pergunta de novo calculo
        c = input("")  # recebe 1 ou 2 para a continuidade ou não do programa
        i = 0  # o i é zerado recebendo novamente o valor 0
        media = 0  # a variavel media tambem é zerada recebendo o valor media
        if c == '2':  # se o valor digitado for igual a '2' então o algoritmo deve se encerrar
            r = 1  # r recebe o valor de 1 e o programa termina
        while r == 0:  # se o r tiver valor 0 então começa um segundo loop, com o objetivo de avaliar se a entrada do
            # c é valida e qual o procedimento a se tomar
            if c != '1' and c != '2':  # se o valor de c for diferente de '1' ou '2', então pede para que se entre um
                # novo valor de c
                print("novo calculo (1-sim 2-nao)")  # é imprimido na tela a pergunta de novo calculo
                c = input("")  # recebe 1 ou 2 para a continuidade ou não do programa
            elif c == '1':  # se c for igual a '1' então r recebe o valor 1 , o laço auxiliar termina e retorna para
                # o laço principal
                r = 1
            elif c == '2':  # caso o valor de c for igual a '2' então o programa le a função break e sai do laço
                # auxiliar, sendo c igual a '2' então o não atinge os parametros do laço principal e o programa é
                # finalizado
                break
