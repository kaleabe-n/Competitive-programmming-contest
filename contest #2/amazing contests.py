    count = int(input())
    results = [int(x) for x in input().split()]
    minn = results[0]
    maxx = results[0]
    ans = 0
    for i in range(1,count):
        if results[i] > maxx:
            maxx = results[i]
            ans+=1
        elif results[i] < minn:
            minn = results[i]
            ans+=1
     
    print(ans)
