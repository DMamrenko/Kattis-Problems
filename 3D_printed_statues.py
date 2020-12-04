#3D Printed Statues
from math import log10, floor
statues = int(input())
if statues <= 3:
    print(statues)
else:
    printers = 1
    while 2**printers < statues:
        printers += 1
    print(printers + 1)
