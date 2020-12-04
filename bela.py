#Bela
dominant = [11, 4, 3, 20, 10, 14, 0, 0]
non_dominant = [11, 4, 3, 2, 10, 0, 0, 0]
numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7']

inp = input().split()
hands, dom = int(inp[0]), inp[1]

answer = 0

for i in range(4*hands):
    card = input()
    number, suit = card[0], card[1]

    #if the suit is dominant
    if suit == dom:
        answer += dominant[numbers.index(number)]
    #if it isn't dominant
    else:
        answer += non_dominant[numbers.index(number)]
 
print(answer)
