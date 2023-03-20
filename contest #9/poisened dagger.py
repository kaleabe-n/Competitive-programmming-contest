t = int(input())
mt = 100**500
for _ in range(t):
    n,h = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    l = 1
    r = h
    while l<=r:
        mid = (l+r)//2
        prev = None
        dmg = 0
        for i,t in enumerate(times):
            if i<len(times)-1:
                dmg+=min(mid,times[i+1]-times[i],mt)
            else:
                dmg+=min(mid,mt)
        if dmg>=h:
            r = mid-1
        else:
            l=mid+1
    print(l)
