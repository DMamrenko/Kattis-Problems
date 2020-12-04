#Completing the Square
from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, op):
        return sqrt((op.x-self.x)**2 + (op.y-self.y)**2)
    
    def display(self):
        return '({}, {})'.format(self.x, self.y)

#This function finds the middle point of the connected points
def findPoint(points):
    xs, ys , fops = [], [], []
    corner = points[0]
    for i in points:
        xs.append(i.x)
        ys.append(i.y)
    for i in range(len(points)):
        ops = points[:i]+points[i+1:]
        if points[i].distance(ops[0]) == points[i].distance(ops[1]):
            corner = points[i]
            fops = ops.copy()    
    x = (fops[0].x + fops[1].x)/2
    y = (fops[0].y + fops[1].y)/2
    midpoint = Point(x, y)
    xdif = midpoint.x-corner.x
    ydif = midpoint.y-corner.y
    return Point(corner.x+int(2*xdif), corner.y+int(2*ydif))
                
points = []
for i in range(3):
    x, y = [int(s) for s in input().split()]
    points.append(Point(x, y))

final = findPoint(points)
print(final.x, final.y)

    


