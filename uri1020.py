id = int(input(""))
ia = id // 365
id = id - ia * 365
im = id // 30
id = id - im * 30
print(f"{ia} ano(s)\n{im} mes(es)\n{id} dia(s)")