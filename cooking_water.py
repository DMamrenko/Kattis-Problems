#Kattis: Cooking Water
iterations = int(input())
a, b = [int(i) for i in input().split()]
st = {i for i in range(a, b+1)}
for i in range(iterations-1):
    a, b = [int(i) for i in input().split()]
    temp = {i for i in range(a, b+1)}
    st = st.intersection(temp)    
print('edward is right') if len(st) == 0 else print('gunilla has a point')