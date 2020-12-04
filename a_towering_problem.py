#A Towering Problem: Kattis

def twoInListSumTo(total, numbers):
    for i in numbers:
        for j in range(len(numbers)):
            if i != j and i < j:
                print(i, '+', numbers[j], '=', i+numbers[j])
    

h1, h2, h3, h4, h5, h6, towerHeight, towerHeight2 = [int(s) for s in input().split()]

twoInListSumTo(towerHeight, [h1, h2, h3, h4, h5, h6])
twoInListSumTo(towerHeight, [h1, h2, h3, h4, h5, h6])


