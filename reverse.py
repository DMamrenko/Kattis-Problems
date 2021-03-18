#Kattis : Reverse @ https://open.kattis.com/problems/ofugsnuid

iterations = int(input())
nums = []
for i in range(iterations):
    nums.append(input())
print(*nums[::-1], sep = '\n')