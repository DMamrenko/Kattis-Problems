#Cold-puter Science
iterations = int(input())
lst = [int(s) for s in input().split()]
output = 0
for i in lst:
    if i < 0:
        output += 1
print(output)
