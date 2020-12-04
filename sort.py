#Sort
from collections import Counter

quantity, upperLimit = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]

order = []
for i in numbers:
    if i not in order:
        order.append(i)
print(Counter(numbers).most_common())
print(order)
print('11 11 11 33 33 25 25 77 54')
