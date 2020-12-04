def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def digit_squared_sum(word):
    total = 0
    for letter in word:
        if letter in "ABCDEF":
            total += ("ABCDEF".index(letter)+10)**2
        else:
            total += int(letter)**2
    return total

iterations = int(input())
for i in range(iterations):
    inp = [int(s) for s in input().split()]
    k = inp[0]
    base = inp[1]
    number = inp[2]
    str_rep = toStr(number, base)
    print(k, digit_squared_sum(str_rep))
