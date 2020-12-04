#Kattis Two-Class Binary Neural Network for Handwritten Digits
import random

one = '1'
none = '0'
string = ''
for i in range(30):
    for j in range(51):
        string += random.choice([one, none])
    print(' '.join(string).replace('0', '-1'))
    string = ''
