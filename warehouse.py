class Order():
    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name
    def display(self):
        return (self.name, self.quantity)




cases = int(input())
for i in range(cases):
    orders = {}
    num_orders = int(input())
    for i in range(num_orders):
        name, quantity = input().split()
        if name in orders:
            orders[name] = orders.get(name)+int(quantity)
            
        else:
            orders[name] = int(quantity)

    orders.sort(key=lambda x: x.quantity, reverse=True)
    print(len(orders))
    for i in orders:
        print(i, orders[i])

            
