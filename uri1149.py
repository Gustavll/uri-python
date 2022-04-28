n = list(map(int,input().split()))
s = 0
i = 1
while n[i] <= 0:
    if n[i] <= 0:
        i += 1
    else:
        break
for c in range(0,n[i],1):
    s += n[0] + c
print(s)

'''x = list(map(int, input().split()))
i = 1
s = 0

while x[i] <= 0:
    if x[i] <= 0:
        i = i + 1
    if x[i] > 0:
        break

for c in range(0, x[i]):
    s = s + x[0] + c

print(s)'''