#Charting Progress
def printChart(lines):
    place = 0
    result = []
    for i in lines:
        if i.count('*') == 0:
            result.append(i)
        else:
            result.append((i.count('.')-place)*'.' + i.count('*')*'*' + place*'.')
            place += i.count('*')
    return result

lines = []
while True:
    try:
        inp = input()
        if inp != "":
            lines.append(inp)
        else:
            print(*printChart(lines), sep='\n')
            lines = []
    except EOFError:
        break
