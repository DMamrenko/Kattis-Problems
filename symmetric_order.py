#Symmetric Order
result_list = []
inp = int(input())
while inp != 0:
    list1 = []
    list2 = []
    for i in range(inp):
        if i%2 == 0:
            list1.append(input())
        else:
            list2.append(input())
    result_list.append(list1 + list2[::-1])
    inp = int(input())
    
for i in range(len(result_list)):
    print("SET", i+1)
    for j in result_list[i]:
        print(j)
