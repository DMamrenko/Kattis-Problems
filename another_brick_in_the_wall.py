#Another Brick in the Wall

#taking in the input
dimensions = [int(s) for s in input().split()]
bricks = [int(s) for s in input().split()]
#breaking up the input into variables
height, width, iterations = dimensions[0], dimensions[1], dimensions[2]

#completed counts progress of row as it builds
completed = 0
#layers counts progress of layers as they build
layers = 0
broken = True

for i in range(iterations):
    if layers == height:
        layers += 1
        break
    else:
        completed += bricks[i]
        if completed > width:
            broken = True
            break
    if completed == width:
        layers += 1
        completed = 0

if layers < height and broken:
    print("NO")
else:
    print("YES")
