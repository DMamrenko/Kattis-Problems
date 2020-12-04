#Tarifa
amount = int(input())
months = int(input())
total = 0
for i in range(months):
    total += int(input())
print(months*amount - total + amount)
