#Veci
from itertools import permutations
inp = input()
p = list(sorted([''.join(p) for p in permutations(inp)]))
if inp == p[-1]:
    print(0)
else:
    for i in p:
        if int(inp) < int(i):
            print(int(i))
            break
