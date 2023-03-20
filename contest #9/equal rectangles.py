import collections

q = int(input())
for _ in range(q):
    n =  int(input())
    lens = [int(x) for x in input().split()]
    s = collections.Counter(lens)
    lens = [x for x in s.keys() if s[x]>=2]
    areas = {}
    maxx = 0
    for i in range(len(lens)):
        area = lens[i]*lens[i]
        count = s[lens[i]]//4
        if area in areas:
            areas[area]+= count
        else:
            areas[area] = count
        maxx = max(maxx,areas[area])

        for j in range(i+1,len(lens)):
            area = lens[j]*lens[i]
            count = min(s[lens[i]]//2,s[lens[j]]//2)
            if area in areas:
                areas[area]+=count
            else:
                areas[area] = count
            maxx = max(maxx,areas[area])

    if maxx>=n:
        print("YES")
    else:
        print("NO")
