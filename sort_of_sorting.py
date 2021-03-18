#Kattis: Sort of Sorting @https://open.kattis.com/problems/sortofsorting
n = int(input())
while n != 0:
    names = []
    for i in range(n):
        names.append(input())
    print(*sorted(names, key = lambda x:x[:2]), sep='\n')
    print()
    n = int(input())

