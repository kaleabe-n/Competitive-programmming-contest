t = int(input())
for _ in range(t):
    minTime = float('inf')
    w,e,c=[int(x) for x in input().split()]
    for i in range(4):
        wtn = i*w
        ean = e*(4-i)+abs(i-c)*e
        wan = abs(4-i)*w
        currMin = min(wtn + wan , wtn+ean)
        minTime = min(minTime,currMin)
    print(minTime)
