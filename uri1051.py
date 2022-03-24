salario = input("")
salario = float(salario)
if 0 <= salario <= 2000:
    print("isento")
if 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
if 3000 < salario <= 4500:
    imposto = (salario - 2000)
    if imposto > 1000:
        imposto = (1000 * 0.08) + ((imposto - 1000) * 0.18)
        print(f"R$ {imposto:.2f}")
if salario > 4500:
    valor = (salario - 4500)
    imposto = (1000 * 0.08) + (1500 * 0.18) + (valor * 0.28)
    print(f"R$ {imposto:.2f}")