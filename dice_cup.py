#Dice Cup
from collections import Counter
inp = [int(s) for s in input().split()]
die1, die2 = inp[0], inp[1]
totals = []
for i in range(1, die1+1):
    for j in range(1, die2+1):
        totals.append(i + j)
results = Counter(totals).most_common(len(totals))
answer = [results[0]]

for i in results[1:]:
    if i[1] == answer[0][1]:
        answer.append(i)
for i in answer:
    print(i[0])
