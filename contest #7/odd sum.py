    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    if sum(arr[:len(arr)//2]) != sum(arr[len(arr)//2:]):
        print(*arr)
    else:
        print(-1)
