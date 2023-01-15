n,k = input().split()
n = int(n)
k = int(k)
lectures = [int(x) for x in input().split()]
active = [int(x) for x in input().split()]
prefix = []
pre = 0
for i in range(n):
    if active[i] == 0:
        pre+=lectures[i]
    prefix.append(pre)
 
maxx = 0
for i in range(n):
    if active[i] == 1:
        maxx+=lectures[i]
maxxFromK = 0
for i in range(n-k+1):
    m = prefix[i+k-1]-prefix[i]+lectures[i] if active[i] == 0 else prefix[i+k-1]-prefix[i]
    maxxFromK = max(maxxFromK,m)
print(maxx+maxxFromK)
