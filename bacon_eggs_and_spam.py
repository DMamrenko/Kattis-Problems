#Kattis: Bacon, Eggs, and Spam

num_customers = int(input())
while num_customers != 0:
    items = []
    dic = {}
    for i in range(num_customers):
        order = input().split()
        customer, food = order[0], list(order[1:])

        dic[customer] = food

        for f in food:
            items.append(f)
    
    items = sorted(list(set(items)))
    final = []
    for food in items:
        names = []
        for name, v in dic.items():
            if food in v:
                names.append(name)
        final.append((food, sorted(names)))

    for food, names in final:
        print(food, end=" ")
        print(*names, sep = ' ')
    print()
    num_customers = int(input())

