#Statistics
line = 1
while True:
    try:
        i = [int(s) for s in input().split()]
        if i != "":
            minimum, maximum = min(i[1:]), max(i[1:])
            range_ = maximum-minimum
            print('Case '+ str(line)+':', minimum, maximum, range_)
            line += 1
    except EOFError:
        break


    

