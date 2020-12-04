#Stand on Zanzibar
inp = int(input())
for i in range(inp):
    turtles = [int(s) for s in input().split()]
    count = 0
    for i in range(1, len(turtles)):
        if turtles[i]>2*turtles[i-1]:
            count += turtles[i]-2*turtles[i-1]
    print(count)
