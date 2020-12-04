#Backspace
line = input()
result = []
for i in range(len(line)):
    if line[i] == '<':
        result = result[:-1]
    else:
        result.append(line[i])

if result != []:
    print(''.join(result))
