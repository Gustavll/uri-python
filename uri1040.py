N1,N2,N3,N4 = input("").split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
if media >= 7 :
    print(f"Media: {media:.1f}")
    print(f"Aluno aprovado.")
elif media < 5 :
    print(f"Media: {media:.1f}")
    print(f"Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print(f"Aluno em exame.")
    N5 = float(input(""))
    print(f"Nota do exame: {N5:.1f}")
    media_total = (media + N5) / 2
    if media_total < 5 :
        print(f"Aluno reprovado.")
    else:
        print("Aluno aprovado.")
        print(f"Media final: {media_total:.1f}")
