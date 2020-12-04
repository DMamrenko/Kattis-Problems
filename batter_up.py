#Batter Up
bats = int(input())
results = [int(s) for s in input().split()]
total = 0
walks = 0
for i in results:
    if i > 0:
        total += i
    if i == -1:
        walks += 1

print(total/(bats-walks))
