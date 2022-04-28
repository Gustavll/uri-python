t = int(input(""))
for i in range(0,t,1):
    j = 0
    pop1,pop2,taxa1,taxa2 = input("").split()
    pop1 = int(pop1)
    pop2 = int(pop2)
    taxa1 = float(taxa1)
    taxa2 = float(taxa2)
    while pop1 <= pop2:
        pop1 += pop1 * (taxa1/100)
        pop2 += pop2 * (taxa2/100)
        pop1 = int(pop1)
        pop2 = int(pop2)
        j += 1
        if j > 100:
            print("Mais de 1 seculo.")
            break
    if j <= 100:
        j = int(j)
        print(f"{j} anos.")
