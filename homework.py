#Kattis: Homework @ https://open.kattis.com/problems/heimavinna

problems = input().split(';')
total = 0

for prob in problems:
    if '-' in prob:
        first, second = prob.split('-')
        total += int(second) - int(first) + 1
    else:
        total += 1
print(total)