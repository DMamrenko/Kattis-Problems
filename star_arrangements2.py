#Star Arrangments
from math import sqrt
                   
inp = int(input())
limit = (inp+1)//2

answers = []

if inp % 2 == 0:
    a = (inp//2)-1
    for i in range(2, limit+1):
        if inp % i == 0:
            answers.append((i, i))
        if (inp % ((2*i)-1) == 0):
            answers.append((i, i-1))
else:  
    for i in range(2, limit+1):
        if inp % i == 0:
            answers.append((i, i))
        if (inp%((2*i)-1) == 0):
            answers.append((i, i-1))
for i in sorted(answers):
    print(i)
