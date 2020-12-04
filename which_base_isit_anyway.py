#Which Base Is It Anyway
#https://open.kattis.com/problems/whichbase
it = int(input())

for i in range(it):
    case, num = input().split()
    if '8' in str(num) or '9' in str(num):
        print(case, 0, num, int(num, 16))
    else:
        print(case, int(num, 8), num, int(num, 16))
