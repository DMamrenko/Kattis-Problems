#Simon Says
it = int(input())
for i in range(it):
    inp = input()
    if 'simon says' in inp:
        print(inp[11:])
    else:
        print()
