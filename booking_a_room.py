#Booking a Room
booked = []
r, n = [int(s) for s in input().split()]
for i in range(n):
    booked.append(int(input()))

if r == n:
    print('too late')
else:
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            break
