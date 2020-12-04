#Soft Passwords: Kattis

numbers = '0123456789'
def reverseCase(string):
    result = ''
    for letter in string:
        if letter in numbers:
            result += letter
        elif letter not in numbers and letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

s = input()
p = input()

if s == p:
    print('Yes')
elif s[0] in numbers and s[1:] == p:
    print('Yes')
elif s[-1] in numbers and s[:-1] == p:
    print('Yes')
elif s == reverseCase(p):
    print('Yes')
else:
    print('No')
    
