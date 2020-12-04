#Cryptographer's Conundrum
inp = input()
count = 0
hold = ""
pieces = []
days = 0
for letter in inp:
    count += 1
    hold += letter
    if count == 3:
        count = 0
        pieces.append(hold)
        hold = ""
for part in pieces:
    if part[0] != "P":
        days += 1
    if part[1] != "E":
        days += 1
    if part[2] != "R":
        days += 1
print(days)
