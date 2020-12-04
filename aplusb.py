from itertools import permutations
import math

iterations = int(input())
data = sorted([int(s) for s in input().split()])
reduced = list(set(data))

answer = 0
if data == reduced:
    perms = list(permutations(reduced, 3))
    for p in perms:
        if p[0] + p[1] == p[2]:
            answer += max(data.count(p[0]), data.count(p[1]), data.count(p[2]))
else:
    perms = list(permutations(data, 3))
    for p in perms:
        if p[0] + p[1] == p[2]:
            answer += 1
            print(p[0], '+', p[1], '=', p[2])
print(answer)
