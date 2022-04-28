n = int(input(""))
nfat = n
for i in range(0, n, 1):
    if n - 1 == 0:
        break
    nfat *= (n - 1)
    n -= 1

print(nfat)