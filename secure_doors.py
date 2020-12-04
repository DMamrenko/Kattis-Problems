#Secure Doors
it = int(input())
people = []
for i in range(it):
    inp = input().split()
    if inp[0] == 'entry' and inp[1] not in people:
        people.append(inp[1])
        print(inp[1], 'entered')
    elif inp[0] == 'entry' and inp[1] in people:
        print(inp[1], 'entered', '(ANOMALY)')
    elif inp[0] == 'exit' and inp[1] in people:
        people.remove(inp[1])
        print(inp[1], 'exited')
    elif inp[0] == 'exit' and inp[1] not in people:
        print(inp[1], 'exited', '(ANOMALY)')
