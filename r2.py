#R2
def average(x, y):
    return (x+y)//2

inputs = input().split()
in1 = int(inputs[0])
avg = int(inputs[1])
in2 = -1000
while average(in1, in2) != avg:
    in2 += 1
print(in2)
