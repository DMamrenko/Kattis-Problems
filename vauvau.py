#Vauvau

#times of agg/calm for 2 dogs
agg1, calm1, agg2, calm2 = [int(s) for s in input().split()]
times = [int(s) for s in input().split()]
attacks = ['none', 'one', 'both']
total1 = agg1 + calm1
total2 = agg2 + calm2
count = 0
for i in times:
    if (i%total1) <= agg1 and (i%total1)!=0:
        count += 1
    if (i%total2) <= agg2 and (i%total2)!=0:
        count += 1
    print(attacks[count])
    count = 0
