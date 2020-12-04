from math import sqrt

#helper functions
def distanceFromOrigin(x, y):
    return sqrt(x**2+y**2)

def pointsFromDistance(distance):
    circles = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    if distance > 200:
        return 0
    else:
        for i in range(10):
            if distance <= circles[i]:
                return i+1

#input/output
testCases = int(input())
for i in range(testCases):
    shots = int(input())
    score = 0
    for i in range(shots):
        print('Shot #', i+1)
        x, y = [int(s) for s in input().split()]
        print(distanceFromOrigin(x, y))
        score += pointsFromDistance(distanceFromOrigin(x, y))
        print('points from distance to origin:', pointsFromDistance(distanceFromOrigin(x, y)))
        print('score:', score)
        print()
    print(score)
