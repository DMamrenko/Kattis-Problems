#Unlock Pattern
from math import sqrt
#distance function
def dist(p1, p2):
    return sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

#find point function
def findPoint(x, pattern):
    for i in range(3):
        for j in range(3):
            if pattern[i][j] == x:
                return (j, i)    
pattern = []
points = []
distance = 0
#adding input to the list
for i in range(3):
    pattern.append([int(s) for s in input().split()])
pattern = pattern[::-1]
#keeping track of the points
for i in range(1, 10):
    points.append(findPoint(i, pattern))
for i in range(1, 9):
    distance += dist(points[i], points[i-1])
print(distance)
