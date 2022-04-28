c = True
grenais = 0
interVitoria = 0
gremioVitoria = 0
empate = 0
while c == True:
    inter,gremio = input("").split()
    inter = int(inter)
    gremio = int(gremio)
    if inter > gremio:
        interVitoria += 1
    elif gremio > inter:
        gremioVitoria += 1
    else:
        empate += 1
    grenais += 1
    while True:
        print("Novo grenal (1-sim 2-nao)")
        r = int(input(""))
        if r == 1:
            break
        if r == 2:
            c = False
            break
print(f"{grenais} grenais")
print(f"Inter:{interVitoria}")
print(f"Gremio:{gremioVitoria}")
print(f"Empates:{empate}")
if interVitoria > gremioVitoria:
    print("Inter venceu mais")
elif gremioVitoria > interVitoria:
    print("Gremio venceu mais")
else: print("Nao houve vencedor")