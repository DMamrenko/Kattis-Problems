#Autori
inp = list(input())
answer = ""
for letter in inp:
    if letter == letter.upper() and letter != "-":
        answer += letter
print(answer)
