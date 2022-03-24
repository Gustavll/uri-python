n = int(input(""))
coe = rat = sap = 0
for i in range(0,n,1):
    exp,c = input("").split()
    exp = int(exp)
    if c == 'C':
        coe += exp
    elif c == 'R':
        rat += exp
    elif c == 'S':
        sap += exp
total = sap + rat + coe
porcC = (coe*100) / total
porcR = (rat*100) / total
porcS = (sap*100) / total
print(f"Total: {total} cobaias\nTotal de coelhos: {coe}\nTotal de ratos: {rat}\nTotal de sapos: {sap}\nPercentual de coelhos: {porcC:.2f} %\nPercentual de ratos: {porcR:.2f} %\nPercentual de sapos: {porcS:.2f} %")
'''print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coe}")
print(f"Total de ratos: {rat}")
print(f"Total de sapos: {sap}")
print(f"Percentual de coelhos: {porcC:.2f}%")
print(f"Percentual de ratos: {porcR:.2f}%")
print(f"Percentual de sapos: {porcS:.2f}%")'''
