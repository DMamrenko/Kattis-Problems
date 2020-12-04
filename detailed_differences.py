#Detailed Differences
iterations = int(input())
for i in range(iterations):
    inp1 = input()
    inp2 = input()
    in1list = list(inp1)
    in2list = list(inp2)
    output = ""
    for index in range(len(in1list)):
        if in1list[index] == in2list[index]:
            output += "."
        else:
            output += "*"

    print(inp1)
    print(inp2)
    print(output)
