hi,hf = input("").split()
hi = int(hi)
hf = int(hf)
if hf > hi:
    ht = hf - hi
    print(f"O JOGO DUROU {ht} HORA(S)")
elif hi > hf:
    ht = (24 - hi) + hf
    print(f"O JOGO DUROU {ht} HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")
