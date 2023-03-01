n,k,q = [int(x) for x in input().split()]
minn = float('inf')
validCount = [0]*200000
for _ in range(n):
    l,r = [int(x) for x in input().split()]
    l-=1
    minn = min(minn,l)
    validCount[l]+=1
    if r<200000:
        validCount[r]-=1
prefix = 0
valid = 0
for i in range(minn,len(validCount)):
    prefix+=validCount[i]
    if prefix>=k:
        valid+=1
    validCount[i] = valid
for _ in range(q):
    l,r = [int(x) for x in input().split()]
    l -=2
    r -=1
    if l>=0:
        print(validCount[r]-validCount[l])
    else:
        print(validCount[r])
