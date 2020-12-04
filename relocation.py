#Relocation

com_it = [int(s) for s in input().split()]
com, it = com_it[0], com_it[1]
loc = [int(s) for s in input().split()]


def one(c, x):
    loc[c-1] = x
def two(first, second):
    print(abs(loc[second-1] - loc[first-1]))
    
for i in range(it):
    inp = [int(s) for s in input().split()]
    fun = inp[0]
    if fun == 1:
        one(inp[1], inp[2])
    else:
        two(inp[1], inp[2])
