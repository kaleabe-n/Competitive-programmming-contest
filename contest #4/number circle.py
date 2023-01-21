n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
ans = [None] * n
left = True
i = 0
for num in nums:
    if left:
        ans[i] = num
    else:
        ans[n-i-1] = num
        i+=1
    left = not left
for i in range(n):
    if ans[i-1] + ans[(i+1)%n] > ans[i]:
        continue
    else:
        print("NO")
        break
else:
    print("YES")
    print(*ans)
    
