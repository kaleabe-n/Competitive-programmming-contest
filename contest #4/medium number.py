    testCount = int(input())
    for _ in range(testCount):
        nums = [int(x) for x in input().split()]
        nums.sort()
        print(nums[1])
