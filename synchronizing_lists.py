#Synchronizing Lists
#Dennis Mamrenko Kattis Assignment 4
n = int(input())
while n != 0:
    numbers, d = [], {}
    for i in range(2*n):
        numbers.append(int(input()))
    keys, values = sorted(numbers[:n]), sorted(numbers[n:])
    for i in range(n):
        d[str(keys[i])] = str(values[i])
    for i in numbers[:n]:
        print(d[str(i)])
    #looking for a new list size n
    n = int(input())
    if n == 0:
        break
    else:
        print()
