#Babelfish
inp = input().split()
dictionary = {}
while inp != []:
    dictionary[inp[1]] = inp[0]
    inp = input().split()
while True:    
    try:
        inp2 = input()
        if inp2 in dictionary:
            print(dictionary[inp2])
        else:
            print('eh')
    except EOFError:
        break
