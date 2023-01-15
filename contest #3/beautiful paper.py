    testCount = int(input())
    for i in range(testCount):
        x1,y1 = input().split()
        x1 = int(x1)
        y1 = int(y1)
        x2,y2 = input().split()
        x2 = int(x2)
        y2 = int(y2)
        
        min1 = min(x1,y1)
        max1 = max(x1,y1)
        min2 = min(x2,y2)
        max2 = max(x2,y2)
        if min1 + min2 == max1 and min1 + min2 == max2:
            print("YES")
        else:
            print("NO")
