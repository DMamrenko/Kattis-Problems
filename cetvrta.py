#Cetvrta
import collections
inputs1 = [int(s) for s in input().split()]
inputs2 = [int(s) for s in input().split()]
inputs3 = [int(s) for s in input().split()]
xs = [inputs1[0], inputs2[0], inputs3[0]]
ys = [inputs1[1], inputs2[1], inputs3[1]]
x = collections.Counter(xs).most_common()[-1]
y = collections.Counter(ys).most_common()[-1]
print(x[0], y[0])
