import math

A,B,C = input("").split()
A = float(A)
B = float(B)
C = float(C)
raiz = (B ** 2) - (4 * A * C)
if not raiz < 0:
    delta = math.sqrt(raiz)
    teste1 = (-B + delta)
    teste2 = (-B - delta)
    if not teste1 == 0 or teste2 == 0:
        x1 = teste1 / (2 * A)
        x2 = teste2 / (2 * A)
        print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")
    else:
        print(f"Impossivel calcular")
else:
    print(f"Impossivel calcular")