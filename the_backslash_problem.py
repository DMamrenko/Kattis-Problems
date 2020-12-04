#The Backslash Problem
def add_backslashes(number, string):
    for i in range(number):
        for j in ['\\', '!', '\"', '$', '%', '&', "\'", '(', ')', '*']:
            string = string.replace(j, "\\"+j)
    return string
commands = []
while True:
    try:
        commands.append(input()) 
    except EOFError:
        break
    
for i in range(len(commands)):
    if i % 2 == 0:
        commands[i] = int(commands[i])
                
for i in range(0, len(commands), 2):
    print(add_backslashes(commands[i], commands[i+1]))
