n = int(input(""))
in1 = 0
out1 = 0
for i in range(0, n, 1):
    x = int(input(""))
    if x in range(10, 20):
        in1 += 1
    else:
        out1 += 1
print(f"{in1} in\n{out1} out")
