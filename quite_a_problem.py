#Quite a Problem
while True:
    try:
        line = input()
        if 'problem' in line.lower():
            print('yes')
        else:
            print('no')
    except EOFError:
        break
    

