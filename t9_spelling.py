#T9 Spelling

def letterToT9(char):
    keys = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    message = ''
    if char == ' ':
        return 0
    else:
        for i in range(len(keys)):
            if char in keys[i]:
                return str(i+2) * (keys[i].index(char)+1)

iterations = int(input())
cases = []
##    for i in range(n):
##        cases.append(input())

for i in range(iterations):
    lets = input()
    message = ' '
    for j in lets:
        addition = str(letterToT9(j))
        if message[-1] == addition[0]:
            message += (' '+addition)
        else:
            message += addition
    print('Case #{}:'.format(i+1) + message)
    

