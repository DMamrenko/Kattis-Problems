#Skener
article = []
new_article = []
dim = [int(s) for s in input().split()]
r, c, zr, zc = dim[0], dim[1], dim[2], dim[3]
for i in range(r):
    article.append(input())
word = ''
for i in range(r):
    for j in range(c):
        word += zc*article[i][j]
    for h in range(zr):
        new_article.append(word)
    word = ''
print(*new_article, sep='\n')
