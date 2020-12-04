

def translate(arr):
    zero = ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx']
    one =  ['....x','....x','....x','....x','....x','....x','....x']
    two =  ['xxxxx','....x','....x','xxxxx','x....','x....','xxxxx']
    three= ['xxxxx','....x','....x','xxxxx','....x','....x','xxxxx']
    four = ['x...x','x...x','x...x','xxxxx','....x','....x','....x']
    five = ['xxxxx','x....','x....','xxxxx','....x','....x','xxxxx']
    six =  ['xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx']
    seven =['xxxxx','....x','....x','....x','....x','....x','....x']
    eight =['xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx']
    nine = ['xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx']
    plus = ['.....','..x..','..x..','xxxxx','..x..','..x..','.....']
    characters = [zero, one, two, three, four, five, six, seven, eight, nine, plus]
    for i in range(len(characters)):
        if characters[i] == arr:
            return i
def rewrite(n):
    zero = ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx']
    one =  ['....x','....x','....x','....x','....x','....x','....x']
    two =  ['xxxxx','....x','....x','xxxxx','x....','x....','xxxxx']
    three= ['xxxxx','....x','....x','xxxxx','....x','....x','xxxxx']
    four = ['x...x','x...x','x...x','xxxxx','....x','....x','....x']
    five = ['xxxxx','x....','x....','xxxxx','....x','....x','xxxxx']
    six =  ['xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx']
    seven =['xxxxx','....x','....x','....x','....x','....x','....x']
    eight =['xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx']
    nine = ['xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx']
    plus = ['.....','..x..','..x..','xxxxx','..x..','..x..','.....']
    characters = [zero, one, two, three, four, five, six, seven, eight, nine, plus]
    return characters[n]

lines = []
new = []
for i in range(7):
    lines.append(input())
    
for i in lines:
    arr = list(i)
    for j in range(len(arr)):
        if (j+1)%6 == 0:
            arr[j]=' '
    result = ''.join(arr).split()
    for j in result:
        new.append(j)
numchars = len(new)//7
characters = [[] for i in range(len(new)//7)]
for i in range(len(new)):
    characters[i%numchars].append(new[i])

expression = []
for i in characters:
    expression.append(translate(i))

plus_sign = expression.index(10)
s1 = ''.join(str(e) for e in expression[0:plus_sign])
s2 = ''.join(str(e) for e in expression[plus_sign+1:])
total = int(s1) + int(s2)

output = []
for i in str(total):
    output.append(rewrite(int(i)))

line = ''
for i in range(len(output)):
    for j in range(7):
        line += output[j][i]+'.'
    print(line[:-1])
    line = ''
