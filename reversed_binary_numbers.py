#Reversed Binary Numbers
inpt = str(bin(int(input())))[2:][::-1]
print(int(inpt, 2))
