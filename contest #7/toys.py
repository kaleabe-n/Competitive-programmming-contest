    from collections import Counter
     
    n,m = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split()]
    prices.sort(reverse=True)
    toys = []
    for i in range(m):
        toys.append(input())
    counts = Counter(toys)
    counts = list(counts.values())
    counts.sort(reverse=True)
    minSum = 0
    maxSum = 0
    i = 0
     
    for c in counts:
        maxSum += prices[i]*c
        i+=1
    prices.reverse()
        
    i = 0
    for c in counts:
        minSum += prices[i]*c
        i+=1
    print(minSum,maxSum)
