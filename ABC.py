#ABC
inp_numbers = [int(s) for s in input().split()]
inp_letters = input()
numbers = sorted(inp_numbers)
smallest, middle, largest = numbers[0], numbers[1], numbers[2]

if inp_letters == "ABC":
    print(smallest, middle, largest)
if inp_letters == "ACB":
    print(smallest, largest, middle)
if inp_letters == "BAC":
    print(middle,smallest, largest)
if inp_letters == "BCA":
    print(middle, largest, smallest)
if inp_letters == "CAB":
    print(largest, smallest, middle)
if inp_letters == "CBA":
    print(largest, middle,  smallest)
