n = int(input(""))
for i in range(0,n,1):
    a,b = input("").split()
    a = int(a)
    b = int(b)
    if b == 0:
        print("divisao impossivel")
        continue
    div = a / b
    print(f"{div:.1f}")