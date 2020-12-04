#Soda Slurper
sodas = [int(s) for s in input().split()]
has, finds, needs = sodas[0], sodas[1], sodas[2]

poss = has + finds
drank = 0
while poss >= needs:
    drank += poss//needs
    poss = poss//needs + poss%needs

print(drank)
