    n= int(input())
    arr=[int(x) for x in input().split()]
    arr.sort()
    l=0
    maxLen=0
    for r in range(len(arr)):
          if arr[r]- arr[l] > 5:
                l+= 1
          maxLen= max(maxLen, r-l+1)
    print(maxLen)
