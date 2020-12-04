from collections import OrderedDict

def list_to_dict(l):
    l = sorted(l)
    f = set(l)
    dictionary = {}
    for i in f:
        dictionary[i] = l.count(i)
    result = OrderedDict(sorted(dictionary.items()))
    return result

    
it = int(input())
animals = []
count = 0
while it != 0:
    animals = []
    for i in range(it):
        given = input().split()
        animals.append(given[-1].lower())
    it = int(input())
    count +=1
    print("List {}:".format(count))
    for k, v in list_to_dict(animals).items():
        print(k, '|', v)

