#Railroad
junctions, switches = [int(s) for s in input().split()]
if switches % 2 == 0:
    print('possible')
else:
    print('impossible')
