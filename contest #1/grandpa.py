    inp = input().split()
    stones = set()
    for stone in inp:
        stones.add(stone)
    if len(stones)>=5:
        print("YES")
    else:
        print("NO")
