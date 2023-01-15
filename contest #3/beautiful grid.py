from collections import Counter
testCount = int(input())
for _ in range(testCount):
    n = int(input())
    grid = []
    for i in range(n):
        grid.append([int(x) for x in input()])
    start = 0
    end = n-2
    i = start
    ans = 0
    for j in range(n//2):
        while i <= end:
            curr = [j,i]
            second = [i,n-j-1]
            third = [second[1],n-second[0]-1]
            forth = [third[1],n-third[0]-1]
            t = grid[curr[0]][curr[1]] == grid[second[0]][second[1]]
            t = t and grid[second[0]][second[1]] == grid[third[0]][third[1]]
            t = t and grid[third[0]][third[1]] == grid[forth[0]][forth[1]]
            # print(curr,second,third,forth)
            if not t:
                arr = []
                arr.append(grid[curr[0]][curr[1]])
                arr.append(grid[second[0]][second[1]])
                arr.append(grid[third[0]][third[1]])
                arr.append(grid[forth[0]][forth[1]])
                c = Counter(arr)
                ans+= min(list(c.values()))
            i+=1
        start += 1
        end -= 1
        i = start
    print(ans)
        
