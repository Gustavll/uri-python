n = float(input(""))
print(f"{n}")
n100 = n // 100
n = n - n100 * 100
print("NOTAS:")
print(f"{n100:.0F} nota(s) de R$ 100.00")
n50 = n//50
n = n - n50 * 50
print(f"{n50:.0F} nota(s) de R$ 50.00")
n20 = n // 20
n = n - n20 * 20
print(f"{n20:.0F} nota(s) de R$ 20.00")
n10 = n // 10
n = n - n10 * 10
print(f"{n10:.0F} nota(s) de R$ 10.00")
n5 = n // 5
n = n - n5 * 5
print(f"{n5:.0F} nota(s) de R$ 5.00")
n2 = n // 2
n = n - n2 * 2
print(f"{n2:.0F} nota(s) de R$ 2.00")
n1 = n // 1
n = n - n1 * 1
print("MOEDAS:")
print(f"{n1:.0F} moeda(s) de R$ 1.00")
n050 = n // 0.50
n = n - n050 * 0.50
print(f"{n050:.0F} moeda(s) de R$ 0.50")
n025 = n // 0.25
n = n - n025 * 0.25
print(f"{n025:.0F} moeda(s) de R$ 0.25")
n010 = n // 0.10
n = n - n010 * 0.10
print(f"{n010:.0F} moeda(s) de R$ 0.10")
n005 = n // 0.05
n = n - n005 * 0.05
print(f"{n005:.0F} moeda(s) de R$ 0.05")
n001 = n // 0.01
n = n - n001 * 0.01
print(f"{n001:.0F} moeda(s) de R$ 0.01")
