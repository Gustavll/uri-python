testes = int(input(""))
for i in range(0,testes,1):
    n = float(input(""))
    if n == 0 :
        print("NULL")
    elif n > 0 :
        if n % 2 == 0:
            print("EVEN POSITIVE")
        elif n % 2 != 0:
            print("ODD POSITIVE")
    else:
        if n % 2 == 0:
            print("EVEN NEGATIVE")
        elif n % 2 != 0:
            print("ODD NEGATIVE")