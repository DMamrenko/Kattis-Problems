#Compound Words
from itertools import permutations
words = []
neww= []
c = []
try:
    while True:
        inp = input()
        if inp != "":
            words.append(inp.split())
        else:
            break
except EOFError:
	pass

for i in words:
    for j in i:
        neww.append(j)
p = list(permutations(neww, 2))

for i in p:
    c.append(i[0]+i[1])

ans = sorted(set(c))
print(*ans, sep='\n')

