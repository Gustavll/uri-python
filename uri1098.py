i = 0  # define o valor de i para 0
j = 1  # define o valor de j para 1
while i <= 2:  # o i termina no numero 2, então enquanto ele for menor ou igual a 2 o loop continua
    for c in range(1, 4):  # o a sequencia acontece 3 vezes para cada i, neste caso o c vai do 1 ao 3
        if i == 1.0 or i == 0.0 or i > 1.8:  # se o i for 1 , o, ou menor que 1.8 . o valor imprimido é o valor
            # inteiro(como o passo do i é 0,2 então quando for maior que 1.8 ou menor que 2 é por que o valor de i é
            # 1.99999998, e nesse caso deve ser arredondado para 2)
            print('I={:.0f} J={:.0f}'.format(i, j))  # imprime o valor de i e j arredondado
        elif i < 2:  # se i for menor que 2 e menor que 1.8 então é levado em consideração uma casa decimal
            print('I={:.1f} J={:.1f}'.format(i, j))  # imprime o valor de i e j arredondado para uma casa
        j += 1  # o jota é acrescido de 1 para cada laço for referente a um valor unico de i
    i += 0.2  # acresce 0.2 no i
    j = 1 + i  # da ao j um novo valor para iniciar, sendo o j sempre 1 a mais que o i
