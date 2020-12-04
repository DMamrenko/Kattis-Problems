#Cudoviste
def find(a):
    answer = [0, 0, 0, 0, 0]
    for i in a:
        if i == '....':
            answer[0] += 1
        else:
            answer[i.count("X")] += 1
    return answer
            
            
dim = [int(s) for s in input().split()]
x, y = dim[0], dim[1]
spots = []
places = []
for i in range(x):
    spots.append(input())
for i in range(x-1):
    for j in range(y-1):
        spot = (spots[i][j:j+2] + spots[i+1][j:j+2])
        if '#' not in spot:
            places.append(spot)
print(*find(places), sep='\n')

