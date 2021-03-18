#Kattis: Electrical Outlets @https://open.kattis.com/problems/electricaloutlets

iterations = int(input())
for i in range(iterations):
    strips = [int(s) for s in input().split()][1:]
    print(sum(strips) - len(strips) + 1)
