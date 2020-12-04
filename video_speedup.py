#Kattis: Video Speedup
#https://open.kattis.com/problems/videospeedup

def get_differences(lst):
    diffs = []
    for i in range(1, len(lst)):
        diffs.append(lst[i]-lst[i-1])
    return diffs


def main():
    #n is #of timestamps, p is speedup percentage, k is length of sped up video

    n, p, k = [int(s) for s in input().split()]
    timestamps = [int(s) for s in input().split()]

    timestamps.append(0)
    timestamps.append(k)
    diffs = get_differences(sorted(timestamps))

    total = 0
    for i in range(len(diffs)):
        total += diffs[i] * (1+i*(p/100))
    print(total)


if __name__ == "__main__":
    main()



