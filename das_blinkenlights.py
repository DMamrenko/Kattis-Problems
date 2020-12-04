#Das Blinkenlights
#take input
x, y, z =  [int(s) for s in input().split()]

def exists(list1, list2):
    for i in range(z):
        if list1[i] == True and list2[i] == True:
            return True
    return False

list1 = [False]*z
list2 = [False]*z
for i in range(x-1, len(list1), x):
    list1[i] = True
for i in range(y-1, len(list2), y):
    list2[i] = True

if exists(list1, list2):
    print('yes')
else:
    print('no')
    
