#Different Distances
import math
inp = [float(s) for s in input().split()]
while inp != [0.0]:
    x1, y1, x2, y2, p = inp[0], inp[1], inp[2], inp[3], inp[4]
    print(format(math.pow(math.pow(abs(x1-x2), p) + math.pow(abs(y1-y2), p), 1/p), '.10f'))
    inp = [float(s) for s in input().split()]
