#Run-Length Encoding, Run!
from collections import OrderedDict
def encode(prompt):
    result = ''
    prev = prompt[0]
    letters = [prompt[0]]
    reps = []
    count = 0
    for letter in prompt:
        if letter == prev:
            count += 1
        else:
            prev = letter
            letters.append(letter)
            reps.append(count)     
            count = 0
    reps.append(count)
    for i in range(1, len(reps)):
        reps[i] += 1
    for i in range(len(reps)):
        result += letters[i]+str(reps[i])
    return result

def decode(prompt):
    result = ""
    for i in range(0, len(prompt)-1, 2):
        result += prompt[i]*int(prompt[i+1])
    return result

        
inp = input().split()
command, prompt = inp[0], inp[1]
if command == "E":
    print(encode(prompt))
else:
    print(decode(prompt))
