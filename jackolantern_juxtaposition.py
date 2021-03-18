#Kattis: Jack-O'-Lantern Juxtaposition @https://open.kattis.com/problems/jackolanternjuxtaposition
nums = [int(s) for s in input().split()]

result = 1
for n in nums:
    result *= n

print(result)