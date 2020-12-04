#Recount
from collections import Counter


inp = ''
votes = []
while inp != '***':
    inp = input()
    votes.append(inp)

commonality = Counter(votes).most_common()
mc_name = commonality[0][0]
mc2_name = commonality[1][0]
mc_amount = commonality[0][1]
mc2_amount = commonality[1][1]

if mc_amount == mc2_amount:
    print('Runoff!')
else:
    print(mc_name)


    
