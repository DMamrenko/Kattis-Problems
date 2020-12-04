#Reverse Rot
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
inp = input()
while inp != '0':
    out = ''
    given = inp.split()
    rot, message = int(given[0]), given[1]
    message = message[::-1]
    for letter in message:
        out += string[(string.index(letter)+rot)%28]
    print(out)
    inp = input()
