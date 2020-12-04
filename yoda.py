#Yoda
n1 = input()[::-1]
n2 = input()[::-1]
length = min(len(n1), len(n2))
#comparing input strings, recording extra digits
leftover = 0
leftf, lefts = '', ''
if len(n1) > len(n2):
    leftover = len(n1) - len(n2)
    leftf = n1[::-1][:leftover]
elif len(n1) < len(n2):
    leftover = len(n2) - len(n1)
    lefts = n2[::-1][:leftover]

ret1 = ''
ret2 = ''
for i in range(length):
    if int(n1[i]) == int(n2[i]):
        ret1 += n1[i]
        ret2 += n2[i]
    if int(n1[i]) > int(n2[i]):
        ret1 += n1[i]
    elif int(n1[i]) < int(n2[i]):
        ret2 += n2[i]

if ret1 == '':
    print('YODA')
else:
    print(int(leftf+ret1[::-1]))
if ret2 == '':
    print('YODA')
else:
    print(int(lefts+ret2[::-1]))

