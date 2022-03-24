n = int(input(""))
for i in range(0,n,1):
    a,b,c = input("").split()
    a = float(a)
    b = float(b)
    c = float(c)
    media = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f"{media:.1f}")
