hi, mi, hf, mf = input("").split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
if hf > hi:
    ht = hf - hi
    if mf > mi:
        mt = mf - mi
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
    elif mi > mf:
        mt = (60 - mi) + mf
        ht = ht - 1
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
elif hi == hf and mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif hi > hf:
    ht = (24 - hi) + hf
    if mf > mi:
        mt = mf - mi
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
    elif mi > mf:
        mt = (60 - mi) + mf
        ht = ht - 1
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
elif hi == hf:
    if mf > mi:
        mt = mf - mi
        ht = hi - hf
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
    elif mi > mf:
        ht = (24 - hi) + hf
        mt = (60 - mi) + mf
        ht = ht - 1
        print(f"O JOGO DUROU {ht} HORA(S) E {mt} MINUTO(S)")
