#Above Average
iterations = int(input())
for i in range(iterations):
    inputs = [int(n) for n in input().split()]
    students = inputs[0]
    total_score = 0
    #calculating the average
    for i in inputs[1:]:
        total_score += i
    average = total_score/students

    
    #finding how many students were above average
    above = 0
    for i in inputs[1:]:
        if i > average:
            above += 1
    print("{}%".format("%.3f" % round((above/students)*100,3), 3))
