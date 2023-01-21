testCount = int(input())
for _ in range(testCount):
    n,k = input().split()
    n = int(n)
    k = int(k)
    nums = [int(x) for x in input().split()]
    start = 0
    count = 0
    for ind in range(len(nums)):
        if ind == 0:
            prev = nums[ind]
            continue
        if nums[ind] * 2 > prev:
            if ind - start>=k:
                count += 1
        else:
            start = ind
        prev = nums[ind]
    print(count)
