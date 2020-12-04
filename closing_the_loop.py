#Closing the Loop: Kattis

def organizeSegments(segments):
    reds, blues = [], []
    for i in segments:
        if i[-1] == 'R':
            reds.append(int(i[:-1]))
        else:
            blues.append(int(i[:-1]))
    return (sorted(reds, reverse = True), sorted(blues, reverse = True))

def resultCaseToString(case, length):
    return 'Case #'+ str(case) + ': ' + str(length)
      

iterations = int(input())
for i in range(iterations):
    numSegments = int(input())
    segments = input().split()
    oSegments = organizeSegments(segments)
    sreds, sblues = oSegments[0], oSegments[1]

    #test if either amount of blues or reds is 0
    if len(sreds) == 0 or len(sblues) == 0:
        print(resultCaseToString(i+1, 0))
    else:
        minSegments = min(len(sreds), len(sblues))
        totalLength = (sum(sreds[:minSegments]) + sum(sblues[:minSegments])) - (minSegments*2)
        print(resultCaseToString(i+1, totalLength))
        
