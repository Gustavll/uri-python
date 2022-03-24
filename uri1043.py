A, B, C = input("").split()
A = float(A)
B = float(B)
C = float(C)
if A < B + C and B < C + A and C < B + A:
    perimetro = C + B + A
    print(f"Perimetro = {perimetro}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area}")