#Boat Parts: Kattis

parts, days = [int(s) for s in input().split()]
bought = []

dayOfFinalReplacement = 0

uniquePartCount = 0
for i in range(days):
    part = input()
    if part not in bought:
        bought.append(part)
        if len(bought) == parts:
            dayOfFinalReplacement = i+1

if dayOfFinalReplacement == 0:
    print('paradox avoided')
else:
    print(dayOfFinalReplacement)
