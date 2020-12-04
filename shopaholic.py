#Shopaholic
it = int(input())
prices = sorted([int(s) for s in input().split()], reverse=True)
discount = 0
if len(prices) < 3:
    print(discount)
else:
    for i in range(2, len(prices), 3):
        discount += prices[i]
    print(discount)
    
    
