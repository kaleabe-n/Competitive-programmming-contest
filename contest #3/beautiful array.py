    n = int(input())
    arr = [int(x) for x in input().split()]
    set1 = []
    set2 = []
    set3 = []
    nCount = 0
    added = False
    oddN = False
    pCount = 0
    for i in arr:
        if i<0:
            nCount += 1
        elif i>0:
            pCount += 1
    if nCount % 2 == 1:
        oddN = True
     
    has2 = False
    for i in arr:
        if i == 0:
            set3.append(str(i))
        elif i > 0:
            set2.append(str(i))
        else:
            if not added:
                set1.append(str(i))
                added = True
            elif oddN:
                set2.append(str(i))
            else:
                if pCount == 0 and has2 == False:
                    set2.append(str(i))
                    if len(set2) == 2:
                        has2 = True
                else:
                    set3.append(str(i))
     
    print(len(set1),end = " ")
    print(" ".join(set1))
    print(len(set2),end = " ")
    print(" ".join(set2))
    print(len(set3),end = " ")
    print(" ".join(set3))
