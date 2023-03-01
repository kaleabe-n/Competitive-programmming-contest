n = int(input())
nums = [int(x) for x in input().split()]
left = 0
right = n-1
leftTime = 0
rightTime = 0
while left<=right:
    if leftTime<=rightTime:
        leftTime+=nums[left]
        left+=1
    else:
        rightTime+=nums[right]
        right-=1
print(left,n-right-1)
