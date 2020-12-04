#Kattis: Conformity 
#https://open.kattis.com/problems/conformity

from collections import Counter

iterations = int(input())
records = []
for i in range(iterations):
    courses = sorted([int(s) for s in input().split()])
    records.append(courses)


elements = [tuple(i) for i in records]
commonality = Counter(elements).most_common()
most_popular_combo = commonality[0][0]
most_popular_count = commonality[0][1]

total = 0
for element in elements:
    if records.count(list(element)) == most_popular_count:
        total += 1
print(total)