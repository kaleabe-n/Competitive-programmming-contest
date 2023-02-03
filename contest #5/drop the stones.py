t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    for j in range(m):
        holder = n-1
        for seeker in range(n -1, -1 ,-1):
            if grid[seeker][j] == "*":
                grid[seeker][j],grid[holder][j] = grid[holder][j],grid[seeker][j]
                holder -= 1
            elif grid[seeker][j] == "o":
                holder = seeker - 1
        
    for row in grid:
        print("".join(row))
