#Alphabet Spam
inp = input()
total = len(inp)
white, lower, upper, symbols = 0, 0, 0, 0
for letter in inp:
    if letter in "abcdefghijklmnopqrstuvwxyz":
        lower += 1
    elif letter in "abcdefghijklmnopqrstuvwxyz".upper():
        upper += 1
    elif letter == "_":
        white += 1
    else:
        symbols += 1
print(white/total)
print(lower/total)
print(upper/total)
print(symbols/total)

