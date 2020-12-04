#Sum Kind of Problem
iterations = int(input())
for i in range(iterations):
    nums = [int(s) for s in input().split()]
    result = "{}".format(nums[0])
    constraint = nums[1]
    pos = int((constraint*(constraint+1))/2)
    odd = constraint**2
    even = pos*2
    print(result, pos, odd, even)
    
