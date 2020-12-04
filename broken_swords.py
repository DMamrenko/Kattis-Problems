#Broken Swords
iterations = int(input())
swords = []
for i in range(iterations):
    swords.append(input())

T, B, L, R = 0, 0, 0, 0
if iterations != 0:
    for i in swords:
        t, b, l, r = int(i[0]), int(i[1]), int(i[2]), int(i[3])
        T += t
        B += b
        L += l
        R += r

TB = (iterations-T)+(iterations-B)
LR = (iterations-L)+(iterations-R)

new_swords = min(TB//2, LR//2)
print(new_swords, TB%new_swords, LR%new_swords)

    
        
