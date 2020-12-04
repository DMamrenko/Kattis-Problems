#Trik
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    return arr

inp = input()
status = [1, 0, 0]
for letter in inp:
    if letter == "A":
        status = swap(status, 0, 1)
    elif letter == "B":
        status = swap(status, 1, 2)
    else:
        status = swap(status, 0, 2)
print(status.index(1)+1) 
        
