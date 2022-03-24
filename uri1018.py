n = int(input(""))
print(f"{n}")
n100 = n // 100
n = n - n100 * 100
print(f"{n100} nota(s) de R$ 100,00")
n50 = n//50
n = n - n50 * 50
print(f"{n50} nota(s) de R$ 50,00")
n20 = n // 20
n = n - n20 * 20
print(f"{n20} nota(s) de R$ 20,00")
n10 = n // 10
n = n - n10 * 10
print(f"{n10} nota(s) de R$ 10,00")
n5 = n // 5
n = n - n5 * 5
print(f"{n5} nota(s) de R$ 5,00")
n2 = n // 2
n = n - n2 * 2
print(f"{n2} nota(s) de R$ 2,00")
n1 = n // 1
n = n - n1 * 1
print(f"{n1} nota(s) de R$ 1,00")