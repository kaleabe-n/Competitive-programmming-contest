    n = int(input())
    nums = [int(x) for x in input().split()]
    negCount = 0
    hasZero = False
    coins = 0
    for num in nums:
        if num < 0:
            coins += -num -1
            negCount += 1
        elif num > 0:
            coins += num - 1
        else:
            coins += 1
            hasZero = True
    if negCount % 2 == 1:
        if not hasZero:
            coins += 2
            
    print(coins)
