t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    initial = input()
    ones = []
    setBy = [0]*n
    ans = ["0"]*n
    for i in range(n):
        if initial[i] == "1":
            ones.append(i)
            setBy[i] = i
            ans[i] = "1"
    for i,ind in enumerate(ones):
        start = max(0,ind-m) if i == 0 else max(ind-m,(ind+ones[i-1])//2)
        end = min(n-1,ind+m) if i == len(ones)-1 else min(ind+m,((ind+ones[i+1])//2))
        for j in range(start,end+1):
            if ans[j] == "0":
                ans[j] = "1"
                setBy[j] = ind
            else:
                if setBy[j] == j:
                    pass
                else:
                    setter = setBy[j]
                    curr = ind
                    if (setter+ind)//2 == j and (setter+ind)%2==0:
                        ans[j] = "0"

    print("".join(ans))
