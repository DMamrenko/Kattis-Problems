#Chanukah Challenge: Kattis

def countCandles(days):
    return days + (days*(days+1))//2

iterations = int(input())
for i in range(iterations):
    n, days = [int(s) for s in input().split()]
    print(n, countCandles(days))
