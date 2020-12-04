#Costume Contest
from collections import Counter
it = int(input())
costumes = []
finalists = []

for i in range(it):
    costumes.append(input())

rankings = Counter(costumes).most_common()[::-1]
lcommon = rankings[0][1]
for i in range(len(rankings)):
    if rankings[i][1] == lcommon:
        finalists.append(rankings[i][0])
    else:
        break

print(*sorted(finalists), sep= '\n')
