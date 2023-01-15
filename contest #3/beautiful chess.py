testCount = int(input())
for _ in range(testCount):
    input()
    grid = []
    for i in range(8):
        grid.append(input())
        
    counts = []
    for row in grid:
        count = 0
        for item in row:
            if item == "#":
                count += 1
        counts.append(count)
    
    for i in range(1,7):
        if counts[i] == 1 and counts[i-1]>1 and counts[i+1] > 1:
            row = i
            break
    
    for i in range(8):
        if grid[row][i] == "#":
            print(row + 1, i + 1)
            break
