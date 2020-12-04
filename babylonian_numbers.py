#Babylonian Numbers
it = int(input())
for i in range(it):
    total = 0
    nums = input().split(',')[::-1]
    for i in range(len(nums)):
        if nums[i] != '':
            total += int(nums[i])*(60**(i))
    print(total)
