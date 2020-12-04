#Akcija
it = int(input())
b = []
total = 0
for i in range(it):
    b.append(int(input()))
b = sorted(b)[::-1]
for i in range(len(b)):
    if (i+1)%3 != 0:
        total += b[i]
print(total)
