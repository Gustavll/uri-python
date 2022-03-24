i = 1
j = 7
acum = 0
while True:
    if i == 9 and j == 13:
        print(f"I={i} J={j}")
        break
    print(f"I={i} J={j}")
    if acum == 2:
        j += 4
        i += 2
        acum = 0
        continue
    acum += 1
    j -= 1