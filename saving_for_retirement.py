#Saving for Retirement

#b = start age of bob
#br = bob retirement age
#bs = amount bob saves each year
#a = start age of alice
#az = amount that alice saves each year
b, br, bs, a, az = [int(s) for s in input().split()]
asaved = 0
bsaved = 0
ayears = 0
for i in range(b, br):
    bsaved += bs
while asaved<=bsaved:
    asaved += az
    ayears += 1

print(a+ayears)

