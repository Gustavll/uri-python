A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
D = (A + B + abs(A - B)) / 2
E = (D + C + abs(D - C)) / 2
print(f"{E:.0f} eh o maior")