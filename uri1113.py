while True:
    m, n = input("").split()
    m = int(m)
    n = int(n)
    if m == n:
        break
    if m >= n:
        print(f"Decrescente")
    elif m < n:
        print(f"Crescente")

