i = 1
j = 7
while True:
    if i == 9 and j == 5:
        print(f"I={i} J={j}")
        break
    print(f"I={i} J={j}")
    if j == 5:
        j = 7
        i += 2
        continue
    j -= 1