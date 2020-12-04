#Kattis: Sideways Sorting

def getColumns(words):
    cols = []
    current = ''
    for i in range(len(words[0])):
        for word in words:
            current+=word[i]
        cols.append(current)
        current = ''
    return sorted(sorted(cols), key=str.upper)

def toRows(words):
    current = ''
    for i in range(len(words[0])):
        for word in words:
            current += word[i]
        print(current)
        current = ''
    print()

def main():
    r, c = [int(s) for s in input().split()]

    while not (r == 0 and c == 0):
        words = []
        for row in range(r):
            words.append(input())
        sideways = getColumns(words)

        toRows(sideways)

        r, c = [int(s) for s in input().split()]

if __name__ == "__main__":
    main()