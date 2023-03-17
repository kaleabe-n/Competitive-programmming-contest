    n,a,b=[int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    prefix = [0]
    p = 0
    for num in arr:
        p+=num
        prefix.append(p)
    count = 0
    for i,num in enumerate(prefix):
        l = i+1
        r = len(prefix)-1
        while l<=r:
            mid = (l+r)//2
            if prefix[mid]-num > a:
                r = mid-1
            elif prefix[mid]-num < a:
                l = mid+1
            else:
                l = mid
                break
        aPos = l
        l = i+1
        r = len(prefix)-1
        while l<=r:
            mid = (l+r)//2
            if prefix[mid]-num > b:
                r = mid-1
            elif prefix[mid]-num < b:
                l = mid+1
            else:
                r = mid
                break
        bPos = r
        if bPos >= aPos:
            count += bPos - aPos + 1
    print(count)
