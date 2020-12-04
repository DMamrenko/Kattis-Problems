import string
alphabet = sorted(list(set(string.ascii_lowercase)))
def missing(string):
    missing_ = ''
    for letter in alphabet:
        if letter not in string.lower():
            missing_+=letter
    return missing_

it = int(input())
for i in range(it):
    inp = input()
    inp = ''.join([i.lower() for i in inp if i.isalpha()])
    if missing(inp) == '':
        print('pangram')
    else:
        print('missing', missing(inp))
        
