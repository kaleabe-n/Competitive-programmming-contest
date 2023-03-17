n,k = [int(x) for x in input().split()]
students = [int(x) for x in input().split()]
students.sort()
 
ans = 0
l = 0
r = len(students)-1
while k>0:
    mid = (l+r)//2
    ans += min(k,mid-l+1)*students[mid]
    k-=min(k,mid-l+1)
    l = mid+1
print(ans)
