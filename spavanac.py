inp = input().split()
hours = int(inp[0])
minutes = int(inp[1])
total_minutes = hours*60 + minutes - 45
if total_minutes > 0:
    print(total_minutes//60, total_minutes%60)
else:
    print(23, total_minutes+60)
