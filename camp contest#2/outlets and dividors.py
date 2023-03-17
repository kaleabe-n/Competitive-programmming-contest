t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    prefix = 2
    if n<=2:
        print(0)
        continue
    for i,num in enumerate(a):
        prefix+=num-1
        if prefix>=n:
            print(i+1)
            break
    else:
        print(-1)
