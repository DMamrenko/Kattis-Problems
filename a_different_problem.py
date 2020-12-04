while True:
    try:
        inputs = [int(s) for s in input().split()]
        print(abs(inputs[0] - inputs[1]))
    except EOFError:
        break
