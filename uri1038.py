
id,qt = input("").split()
id = int(id)
qt = int(qt)
if id == 1:
    total = 4 * qt
    print(f"Total: R$ {total:.2f}")
elif id == 2:
    total = 4.5 * qt
    print(f"Total: R$ {total:.2f}")
elif id == 3:
    total = 5 * qt
    print(f"Total: R$ {total:.2f}")
elif id == 4:
    total = 2 * qt
    print(f"Total: R$ {total:.2f}")
elif id == 5:
    total = 1.5 * qt
    print(f"Total: R$ {total:.2f}")

