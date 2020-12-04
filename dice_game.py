Gunnar = [int(s) for s in input().split()]
Emma = [int(s) for s in input().split()]
gsum = sum(Gunnar)
esum = sum(Emma)

if gsum > esum:
    print("Gunnar")
elif esum > gsum:
    print("Emma")
else:
    print("Tie")
