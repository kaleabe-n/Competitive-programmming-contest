n = int(input())
arr = [int(x) for x in input().split()]
prev = float('-inf')
maxCount = 0 
count = 0
for num in arr:
    if num < prev:
        count = 1
    else:
        count +=1
        maxCount = max(maxCount,count)
    prev = num

print(maxCount)
