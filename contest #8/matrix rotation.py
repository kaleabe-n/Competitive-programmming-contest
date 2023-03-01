testCount = int(input())
 
 
def isBeautiful(grid):
    if grid[0][0] >= grid[0][1]:
        return False
    if grid[0][0] >= grid[1][0]:
        return False
    if grid[0][1] >= grid[1][1]:
        return False
    if grid[1][0] >= grid[1][1]:
        return False
    return True
    
    
    
def rotate(grid):
    grid[0][0],grid[1][0] = grid[1][0],grid[0][0]
    grid[1][1],grid[1][0] = grid[1][0],grid[1][1]
    grid[1][1],grid[0][1] = grid[0][1],grid[1][1]
    
    
    
for _ in range(testCount):
    grid  = []
    for _ in range(2):
        grid.append([int(x) for x in input().split()])
    for _ in range(5):
        if isBeautiful(grid):
            print("YES")
            break
        rotate(grid)
    else:
        print("NO")
    
