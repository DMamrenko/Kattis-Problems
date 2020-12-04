#ACM Contest Submissions
inp = input().split()
wrong = []
correct = 0
score = 0
while inp != ['-1']:
    time, question, status = int(inp[0]), inp[1], inp[2]
    if status == 'wrong':
        wrong.append(question)
    elif status == 'right':
        correct += 1
        score += (time + 20*wrong.count(question))
    inp = input().split()
print(correct, score)
