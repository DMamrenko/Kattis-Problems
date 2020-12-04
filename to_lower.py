#ToLower
def check(a):
    for element in a:
        if element.lower() != element[0].lower()+element[1:]:
            return False
    return True 

#User Input and Splitting up into Variables
it = [int(s) for s in input().split()]
P, T = it[0], it[1]

correct = 0
inputs = []
hold = []
for i in range(P):
    for j in range(T):
        hold.append(input())
    inputs.append(hold)
    hold = []

for i in range(P):
    if check(inputs[i]):
        correct += 1
        
print(correct)
