A, B, C = input("").split()
A = int(A)
B = int(B)
C = int(C)
if A < B < C:
    print(f"{A}\n{B}\n{C}")
elif A < C < B:
    print(f"{A}\n{C}\n{B}")
elif B < A < C:
    print(f"{B}\n{A}\n{C}")
elif B < C < A:
    print(f"{B}\n{C}\n{A}")
elif C < A < B:
    print(f"{C}\n{A}\n{B}")
elif C < B < A:
    print(f"{C}\n{B}\n{A}")
print(" ")
print(f'{A}\n{B}\n{C}')

'''x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)


if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b
print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)'''