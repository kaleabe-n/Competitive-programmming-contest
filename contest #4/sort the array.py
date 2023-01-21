    length = int(input())
    arr = [int(x) for x in input().split()]
    prev = float("-inf")
    start = None
    maxOfRv = None
    end = None
    for ind,num in enumerate(arr):
        if num < prev and start is None:
            start = ind - 1
            maxOfRv = prev
            end = ind
        if start is not None and maxOfRv > num:
            end = ind
        prev = num
    if start is None:
        start = 0
        end = 0
    sortedArr = sorted(arr)
    rv = arr[start:end+1]
    rv.reverse()
    newArr = arr[:start] + rv + arr[end+1:]
    if newArr == sortedArr:
        print("yes")
        print(start + 1, end + 1)
    else:
        print("no")
