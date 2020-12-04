#Basketball One-on-One: Kattis

game = input()
A, B = 0, 0
for i in range(len(game)//2):
    if game[i*2] == 'A':
        A += int(game[i*2 + 1])
    else:
        B += int(game[i*2 + 1])

if max(A, B) == A:
    print('A')
else:
    print('B')
