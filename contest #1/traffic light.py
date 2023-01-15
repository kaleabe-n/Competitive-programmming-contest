    testCount = int(input())
    for i in range(testCount):
        size,curr = input().split()
        size = int(size)
        lights = input()
        i = 0
        state = False
        maxCount = 0
        toBreak = False
        if curr == "g":
            print(0)
            continue
        while state or i<len(lights):
            if i>=len(lights):
                toBreak = True
                i = i%len(lights)
            if lights[i] == curr and not state:
                count = 0
                state = True
            elif lights[i] == "g" and state:
                count+=1
                maxCount = max(count,maxCount)
                state = False
                count = 0
                if toBreak:
                    break
            elif state:
                count+=1
            i+=1
        print(maxCount)
