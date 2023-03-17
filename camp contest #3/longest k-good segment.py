n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
window = {}
l = 0
longestLen = 0
ends = []
for r,num in enumerate(arr):
    if num in window:
        window[num]+=1
    else:
        window[num] = 1
    while len(window)>k:
        window[arr[l]]-=1
        if window[arr[l]] == 0:
            del window[arr[l]]
        l+=1
    if r-l+1>longestLen:
        longestLen = r-l+1
        ends = [str(l+1),str(r+1)]

print(" ".join(ends))
