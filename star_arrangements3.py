#Star Arrangements
inp = int(input())
limit = (inp+1)//2

answers = []

for i in range(2, limit+1):
    a = i
    b = i-1
    c = a+b
    if inp%a == 0:
        answers.append((a, a))
    if inp%c == 0:
        answers.append((a, b))
    else:
        d = inp//c
        if c*d + a == inp:
            answers.append((a, b))
print(str(inp)+':')
for i in sorted(answers):
    print(str(i[0])+','+str(i[1]))
