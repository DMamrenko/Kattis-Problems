#The Owl and The Fox
def sumd(n):
    total = 0
    s = str(n)
    for i in range(len(s)):
        total += int(s[i])
    return total

def find(n):
    if sumd(n) == 1:
        return 0
    elif n%100 == 0:
        start = n-100
        while sumd(start) != sumd(n)-1:
            start -= 100
        return start
    elif n%10 == 0:
        return n-10
    else:
        return n-1

it = int(input())
for i in range(it):
    start = int(input())
    print(find(start))
