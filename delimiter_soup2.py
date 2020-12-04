#Delimiter Soup

size = int(input())
line = input()
myStack = []

found = False
for character in range(size):
    if line[character] in ']})':
        if len(myStack) == 0:
            print(line[character], character)
            found = True

        else:
            oldestOpener = myStack.pop()
            if (line[character] == ')' and oldestOpener != '(') or (line[character] == '}' and oldestOpener != '{') or(line[character] == ']' and oldestOpener != '['):
                found = True
                print(line[character], character)
                break
    elif line[character] in '[{(':
        myStack.append(line[character])
if found == False:
    print('ok so far')
