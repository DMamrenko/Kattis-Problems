#Black Friday
from collections import Counter

#taking input
inp = int(input())
rolls = [int(s) for s in input().split()]
st = list(set(rolls))[::-1]
unicount = sorted(Counter(rolls).most_common())

#Check if the list contains a unique entity
unique = False
for i in unicount:
    if i[1] == 1:
        unique = True
        break
print(st)
#printing the highest unique number
if len(st) == 1 or unique == False:
    print('none')
else:
    for i in range(len(st)):
        if rolls.count(st[i]) == 1:
            print(rolls.index(st[i])+1)
            break

        
