t = int(input())
for _ in range(t):
    n = int(input())
    weights = [int(x) for x in input().split()]
    prefixSum = []
    p = 0
    for num in weights:
        p+=num
        prefixSum.append(p)
    if n < 12:
        print(p)
        continue
    minn = prefixSum[11]
    for i in range(11,n-1,6):
        r = min(n-1,i+12)
        minn = min(minn,prefixSum[r]-prefixSum[i])
    print(minn)
