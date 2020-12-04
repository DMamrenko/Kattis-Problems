#Convex Polygon Area

def PolygonArea(X, Y, numPoints):
    area = 0
    j = numPoints-1
    for i in range(numPoints):
        area += (X[j]+X[i]) * (Y[j]-Y[i])
        j = i
    return abs(area/2)

it = int(input())

for i in range(it):
    Xs = []
    Ys = []
    numbers = [int(s) for s in input().split()]
    vertices = numbers[0]
    for i in range(1, len(numbers)):
        if i%2 == 1:
            Xs.append(numbers[i])
        else:
            Ys.append(numbers[i])
    print(PolygonArea(Xs, Ys, vertices))
    
