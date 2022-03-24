vertebra = input("")
tipo = input("")
alimento = input("")
if 'in' in vertebra:
    if 'inseto' in tipo:
        if 'hematofago' in alimento:
            print("pulga")
        if 'herbivoro' in alimento:
            print("lagarta")
    if 'anelideo' in tipo:
        if 'hematofago' in alimento:
            print("sanguessuga")
        if 'onivoro' in alimento:
            print("minhoca")
else:
    if 'ave' in tipo:
        if 'carnivoro' in alimento:
            print("aguia")
        if 'onivoro' in alimento:
            print("pomba")
    if 'mamifero' in tipo:
        if 'onivoro' in alimento:
            print("homem")
        if 'herbivoro' in alimento:
            print("vaca")
