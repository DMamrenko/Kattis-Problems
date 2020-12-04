#Skocimis
x = [int(s) for s in input().split()]
A, B, C = x[0], x[1], x[2]
print(max((B-A-1), (C-B-1)))
