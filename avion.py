lines = []
hits = []
for i in range(5):
    lines.append(input())

for i in range(len(lines)):
    if "FBI" in lines[i]:
        hits.append(i+1)

if len(hits) == 0:
    print("HE GOT AWAY!")
else:
    print(*hits, sep = ' ')
        
        
