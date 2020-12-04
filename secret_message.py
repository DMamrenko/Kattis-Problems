#Secret Message
from math import sqrt
from MatrixTransformations import *

#size to box
def sizeNeeded(n):
    i = 1
    while i < sqrt(n):
        i += 1
    return i

def createArray(string):
    array = []
    size = sizeNeeded(len(string))
    for i in range(0, len(string), size):
        array.append(list(string[i:i+size]))
    return array           

iterations = int(input())
for i in range(iterations):
    inp = input()
    ogSize = len(inp)
    newSize = sizeNeeded(len(inp))**2
    inp = inp+(newSize-ogSize)*'*'
    #print('given input:', inp)
    encoded = createArray(inp)
    #print(*encoded, sep='\n')
    newArray = rotateRight(encoded)

    result = ''
    for i in newArray:
        result += i.strip('*')
    print(result)
