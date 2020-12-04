#Speed Limit

inp = int(input())
total_miles = 0
while inp != -1:
    total_hours = 0
    for i in range(inp):
        values = input().split()
        total_miles += int(values[0])*(int(values[1])-total_hours)
        total_hours += int(values[1])-total_hours
    print("{} miles".format(total_miles))
    total_miles = 0
    inp = int(input())
