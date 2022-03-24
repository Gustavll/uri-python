A,B,C = input().split()
pi = 3.14159
A = float(A)
B = float(B)
C = float(C)
area_triang = (A * C) / 2
area_circ = pi * (C ** 2)
area_trape = ((A + B) * C ) / 2
area_quadra = B ** 2
area_ret = A * B
print(f"TRIANGULO: {area_triang:.3f}\nCIRCULO: {area_circ:.3f}\nTRAPEZIO: {area_trape:.3f}\nQUADRADO: {area_quadra:.3f}\nRETANGULO: {area_ret:.3f}")
