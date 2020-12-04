#The Easiest Problem Is This One

#This function calculates a products digit sum
def sum_digits_product(x, y):
    z = x*y
    sum_ = 0
    for letter in str(z):
        sum_ += int(letter)
    return sum_

#This function calculates the value p Kattis is looking for
def calculate_p(N):
    current = 11
    test = sum_digits_product(current, N)
    while test != sum_digits_product(N, 1):
        current += 1
        test = sum_digits_product(current, N)
    return current


N = int(input())
while N != 0:
    print(calculate_p(N))
    N = int(input())


