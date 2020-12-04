#Kattis: Triple Texting
from collections import Counter

triple = input()
length = len(triple)//3

words = [triple[0:length], triple[length:length*2], triple[length*2:]]
print(Counter(words).most_common()[0][0])
