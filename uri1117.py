i = 0  # define o valor de 1 como 0
med = 0  # define a variavel para calculo da media como 0
while i < 2:  # enquanto o i for menor que 2
    nota = float(input())  # recebe o valor da nota
    if 0 <= nota <= 10:  # se a nota foi positiva ou igual a zero, e menor ou igual a 10
        i += 1  # acrescenta 1 em i
        med += nota  # e acrescenta o valor da nota da variavel para calculo da media
    if nota < 0 or nota > 10:  # se a nota é negativa ou maior que 10, então imprime nota invalida é recomeça o codigo
        print('nota invalida')
med = med / 2  # após o final do laço, os valores armazenados na variavel para calculo da media são divididos pela
# sua quantidade de termos
print('media = {:.2f}'.format(med))  # por fim a media total é imprimida com duas casas decimais
