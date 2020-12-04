#Ragged Right
lines = []
while True:
    try:
        lines.append(len(input()))
    except EOFError:
        break
longest = max(lines)
answer = 0
for line in lines[:len(lines)-1]:
    answer += (longest - line)**2
print(answer)
