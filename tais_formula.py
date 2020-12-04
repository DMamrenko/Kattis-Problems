#Tai's Formula

iterations = int(input())
data = []
result = 0

for i in range(iterations):
    entry = input().split()
    data.append( (int(entry[0]), float(entry[1])) )
for i in range(1, iterations):
    result += ((data[i][1] + data[i-1][1])/2)*(data[i][0]-data[i-1][0])

print(result/1000)    
