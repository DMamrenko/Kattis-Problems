instances = int(input())
answer = 0
for i in range(instances):
    inputs = input().split()
    answer += float(inputs[0])*float(inputs[1])
print(answer)
