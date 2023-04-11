n,m,k = [int(x) for x in input().split()]
grid = []
ans = 0
colCount = [0]*m
for i in range(n):
    rowCount = 0
    row = input()
    for i,letter in enumerate(row):
        if letter == ".":
            rowCount += 1
            colCount[i]+=1
        else:
            rowCount = 0
            colCount[i] = 0
        if rowCount >= k:
            ans+=1
        if colCount[i]>=k:
            ans+=1
if k == 1:
    print(ans//2)
else:
    print(ans)
    
