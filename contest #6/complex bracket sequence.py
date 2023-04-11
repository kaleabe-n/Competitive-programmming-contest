s = input()
left = 0
right = len(s) - 1
ans = []

while (left < right):
    while (left < right and s[left] == ')'):
        left += 1
        
    while (left < right and s[right] == '('):
        right -= 1
    
    if (left < right):
        ans.append(left + 1)
        ans.append(right + 1)
    
    left += 1
    right -= 1

ans.sort()

if (len(ans) > 0):
    print(1)
    print(len(ans))
    print(*ans)
else:
    print(0)
