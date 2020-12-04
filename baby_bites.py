#Baby Bites
from collections import Counter
numbers = int(input())
words = [str(s) for s in input().split()]

boolean = True
for i in range(len(words)):
    if words[i] != str(i+1):
        if words[i] != "mumble":
            boolean = False
            break

if boolean == True:
    print("makes sense")
else:
    print("something is fishy")
