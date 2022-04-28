alcool = 0
gasolina = 0
disel = 0
j = 0
while j == 0:
        n = int(input(""))
        if n == 1:
            alcool += 1
        elif n == 2:
            gasolina += 1
        elif n == 3:
            disel += 1
        elif n == 4:
            j = 1
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {disel}")