id1, q1, v1 = input().split(" ")
id2, q2, v2 = input().split(" ")



total = (int(q1) * float(v1)) + (int(q2) * float(v2))

print(f"VALOR A PAGAR: R$ {total:.2f}")