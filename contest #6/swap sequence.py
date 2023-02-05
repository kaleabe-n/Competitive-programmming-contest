    n = int(input())
    nums = [int(x) for x in input().split()]
    swaps = []
    for i in range(n):
        minn = float('inf')
        minInd = None
        for j in range(i,n):
            if nums[j] < minn:
                minn = nums[j]
                minInd = j
        if minInd != i:
            swaps.append([i,minInd])
            nums[i],nums[minInd] = nums[minInd],nums[i]
    print(len(swaps))
    for i,j in swaps:
        print(i,j)
