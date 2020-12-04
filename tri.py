#Tri
inp = [int(s) for s in input().split()]
first, second, third = inp[0], inp[1], inp[2]
if first + second == third:
    print("{}+{}={}".format(first, second, third))
elif first - second == third:
    print("{}-{}={}".format(first, second, third))
elif first // second == third:
    print("{}/{}={}".format(first, second, third))
elif first * second == third:
    print("{}*{}={}".format(first, second, third))
elif first == second + third:
    print("{}={}+{}".format(first, second, third))
elif first == second - third:
    print("{}={}-{}".format(first, second, third))
elif first == second // third:
    print("{}={}/{}".format(first, second, third))
elif first == second * third:
    print("{}={}*{}".format(first, second, third))
