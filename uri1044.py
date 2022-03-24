A, B = input("").split()
A = int(A)
B = int(B)
if A % B == 0 or B % A == 0:
    print(f'Sao multiplos')
else:
    print('Nao sao multiplos')
