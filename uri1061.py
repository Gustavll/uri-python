dia_i = input().split()  # cria um vetor que armazena a string dia, e o valor referente ao dia
hora_i = input().split()  # cria um vetor que armazena a hora minuto e segundo, bem como a separação de sintaxe(:)
dia_f = input().split()  # cria um vetor que armazena a string dia, e o valor referente ao dia
hora_f = input().split()  # cria um vetor que armazena a hora minuto e segundo, bem como a separação de sintaxe(:)

di, df = int(dia_i[1]), int(dia_f[1])  # duas variaveis transformam em inteiro e depois buscam na lista ultilizando
# index os valores dos dias
hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])  # tres variaveis transformam em inteiro e depois buscam
# na lista a hora minuto e segundo ultilizando os valores do index
hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4])  # tres variaveis transformam em inteiro e depois buscam
# na lista a hora minuto e segundo ultilizando os valores do index
minuto_seg = 60  # cria a variavel referente a quantos segundo tem um minuto para fins de calculo
hora_seg = minuto_seg * 60  # cria uma variavel referente a quantos segundos tem uma hora
dia_seg = hora_seg * 24  # cria uma variavel referente a quantos segundos tem um dia
i = si + mi * minuto_seg + hi * hora_seg + di * dia_seg  # transforma em segundos os dados do inicio obtidos em forma de
# dias, horas, minutos e segundos
f = sf + mf * minuto_seg + hf * hora_seg + df * dia_seg  # transforma em segundos os dados do final obtidos em forma de
# dias, horas, minutos e segundos
if i < f:  # compara o valor em segundos do inicio com o valor em segundos do final, caso o final seja menor que o
    # inicio então os dados inseridos estão incorretos, caso o valor final seja maior q o incial então:
    tempo = f - i  # o tempo total é o final menos o inicial
    dias = int(tempo / dia_seg)  # cria uma variavel dias que armazena em forma de inteiro a divisão entre o tempo
    # total e os dias em segundos
    tempo = tempo % dia_seg  # o tempo agora se torna o resto da divisão entre o tempo total e o dia em segundos
    horas = int(tempo / hora_seg)  # cria uma variavel horas que armazena em forma de inteiro a divisão entre o tempo
    # total e as horas em segundos
    tempo = tempo % hora_seg  # o tempo agora se torna o resto da divisão entre o tempo total e as horas em segundos
    minutos = int(tempo / minuto_seg)  # cria uma variavel minutos que armazena em forma de inteiro a divisão entre o
    # tempo total e os minutos em segundos
    tempo = tempo % minuto_seg  # o tempo agora se torna o rewsto da divisão entre o tempo total e os minutos em segundos
    segundos = tempo  # por fim a variavel segundos recebe o que sobrou do tempo após as divisões : os segundos
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
    # imprime na tela o dia, as horas,os minutos e os segundos
