#Card Trick

master_string = 'abcdefghijklm'
def bottom(times, cards):
    new = []
    for i in range(times):
        top = cards[0]
        tail = cards[1:]
        new = tail+top
        cards = new
    return new

def getAlphaOrder(numCards):
    alphaList = master_string[:numCards]
    order = []
    for i in range(1, numCards+1):
        if i == numCards:
            order.append(alphaList[0])
        else:
            alphaList = bottom(i, alphaList)
            order.append(alphaList[0])
            alphaList = alphaList[1:]
    return order

def getNumericalOrder(order):
    result = [0]*len(order)
    letters = master_string[0:len(order)]
    for i in range(len(letters)):
        for j in order:
            if letters[i]==j:
                result[i] = order.index(j)+1
    return result

#all input/output/function calls
iterations = int(input())
for i in range(iterations):
    alphabetic = getAlphaOrder(int(input()))
    finalOrder = getNumericalOrder(alphabetic)
    print(*finalOrder, sep=' ')


