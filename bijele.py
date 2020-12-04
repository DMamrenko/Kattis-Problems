#Bijele
inputs = input().split()
correct = [1, 1, 2, 2, 2, 8]
answer = []
for i in range(len(inputs)):
    answer.append(correct[i]-int(inputs[i]))
print(" ".join(str(x) for x in answer))
