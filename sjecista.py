#Sjecista
from math import factorial

inp = int(input())
if inp == 3:
    print(0)
else:
    print(int(factorial(inp)/(factorial(4)*factorial(inp-4))))
