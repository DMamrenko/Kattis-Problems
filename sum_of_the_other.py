#Sum of the Others
while True:
    try:
        line = [int(s) for s in input().split()]
        for i in range(len(line)):
            others = line[:i]+line[i+1:]
            sum_ = sum(others)
            if line[i] == sum_:
                print(line[i])
                break
    except EOFError:
        break
