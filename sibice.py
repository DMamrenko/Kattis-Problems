#Sibice
import math
inp = input().split()
matches = int(inp[0])
max_size = math.sqrt(int(inp[1])**2 + int(inp[2])**2)

for i in range(matches):
    input_ = int(input())
    if input_ <= max_size:
        print("DA")
    else:
        print("NE")
