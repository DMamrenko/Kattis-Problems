#Traveling Salesperson 2D
import math
import itertools

def distance(x, y, x1, y1):
    return(int(math.sqrt((y1 - y)**2 + (x2-x)**2)))

iterations = int(input())
points = []
indexes = []
start = 0
min_distance = 1000000
for i in range(iterations):
    points.append([float(s) for s in input().split()])

combos = itertools.combinations(points, 2)

for i in list(combos):
    print(i)
