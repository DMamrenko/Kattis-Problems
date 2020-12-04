#Cetiri

#Sorting the given 3 integers and splitting into variables
x = sorted([int(s) for s in input().split()])
a, b, c = x[0], x[1], x[2]

diffab = abs(b-a)
diffbc = abs(c-b)

if diffab == diffbc:
    print(c + diffbc)
else:
    if diffab > diffbc:
        print(a + diffbc)
    elif diffab < diffbc:
        print(b + diffab)
