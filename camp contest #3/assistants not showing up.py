n,m = [int(x) for x in input().split()]
prefix = [0]*n
for _ in range(m):
    l,r = [int(x) for x in input().split()]
    prefix[l]+=1
    if r+1 < n:
        prefix[r+1]-=1

p = 0
for num in prefix:
    p+=num
    if p == 0:
        print("YES")
        break
else:
    print("NO")
