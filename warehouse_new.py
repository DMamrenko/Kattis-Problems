#Warehouse: Kattis
from operator import attrgetter
from operator import itemgetter

class whEntry():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def getName(self):
        return self.name
        
    def show_entry(self):
        return self.name + ' ' + str(self.quantity)

class WareHouse():
    def __init__(self, inventory):
        self.inventory = inventory

    def addItem(self, item):
        exists = False
        if isinstance(item, whEntry):
            for entry in self.inventory:
                if entry.name == item.name:
                    exists = True
                    entry.quantity += item.quantity
        if not exists:
            self.inventory.append(item)

    def sortInventory(self):
        s = sorted(self.inventory, key=attrgetter('name'))
        self.inventory = sorted(s, key=attrgetter('quantity'), reverse = True)
        return self.inventory
     
    def show_warehouse(self):
        for item in self.inventory:
            print(item.show_entry())
            

iterations = int(input())
for i in range(iterations):
    numItems = int(input())

    inv = []
    wh = WareHouse(inv)
    for i in range(numItems):
        inp = input().split()
        name, quantity = inp[0], int(inp[1])
        item = whEntry(name, quantity)
        wh.addItem(item)
        
    wh.sortInventory()
    print(len(wh.inventory))
    wh.show_warehouse()
    


    


