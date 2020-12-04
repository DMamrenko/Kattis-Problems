#Stacking Cups
iterations = int(input())
final = []
sizes = []
for i in range(iterations):
    try:#if the input is radius, color
        inputs = input().split()
        color, radius = inputs[0], float(inputs[1])
    except ValueError:#if the input is color, diameter
        radius, color = float(inputs[0])/2, inputs[1]
    sizes.append(radius)
    final.append((radius, color))
answer = sorted(final)
for i in range(len(answer)):
    print(answer[i][1])
