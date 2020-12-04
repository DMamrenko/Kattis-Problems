#Zamka
def sum_digits(n):
    result = 0
    for digit in str(n):
        result += int(digit)
    return result
        
L = int(input())#lower bound
D = int(input())#upper bound
X = int(input())#target

for i in range(L, D+1):
    if sum_digits(i) == X:
        print(i)
        break
for i in range(D, L-1, -1):
    if sum_digits(i) == X:
        print(i)
        break
