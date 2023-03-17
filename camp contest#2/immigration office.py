n = int(input())
que = input().split()
q = int(input())
for _ in range(q):
    newName = input()
    l = 0
    r = len(que)-1
    while l<=r:
        mid = (l+r)//2
        if que[mid] >= newName:
            r = mid-1
        else:
            l = mid+1
    print(l)
