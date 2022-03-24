A, B, C = input("").split()
A = float(A)
B = float(B)
C = float(C)
E = float(1)
F = float(1)
G = float(1)

if A >= B and A>= C:
    E = A
    if B >= C:
        F = B
        G = C
    else:
        F = C
        G = B
if B >= A and B >= C:
    E = B
    if A >= C:
        F = A
        G = C
    else:
        F = C
        G = A
if C >= A and C>= B:
    E = C
    if B >= A:
        F = B
        G = A
    else:
        F = A
        G = B

print(f"{E}")
print(f"{F}")
print(f"{G}")
if E >= F + G:
    print("NAO FORMA TRIANGULO")
else:
    if (E**2) == (F**2) + (G**2):
        print("TRIANGULO RETANGULO")
    if (E**2) > (F**2) + (G**2):
        print("TRIANGULO OBTUSANGULO")
    if (E**2) < (F**2) + (G**2):
        print("TRIANGULO ACUTANGULO")
    if E == F == G:
        print("TRIANGULO EQUILATERO")
    if E == F and E != G or E == G and E != F or F == G and G != E:
        print("TRIANGULO ISOSCELES")






        '''if A == B == C:
            F = G = A
        elif A == C and B > C:
            G = C
            F = A
            A = B
        elif A == C and B < C:
            G = B
            F = C
        elif A == B and C > B:
            G = B
            F = A
            A = C
        elif A == B and C < B:
            G = C
            F = A
        elif A > C and C > B:
            G = B
            F = C
        elif A > C and C < B:
            G = C
            if A > B:
                F = B
            if A < B:
                F = A
                A = B
        elif A > C == B:
            G = B
            F = C
        elif A < C and B > C:
            G = A
            F = C
            A = B
        elif A < C == B:'''






