t=int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    zeros = []
    for ind,num in enumerate(arr):
        if num == 0:
            zeros.append(ind)
    
    ops = 0
    zerosInd = 0
    for ind,num in enumerate(arr):
        if ind == len(arr)-1:
            break
        if num != 0:
            if len(zeros) == 0:
                ops+=num
            else:
                while num>0 and zerosInd<len(zeros):
                    while zerosInd<len(zeros) and ind>=zeros[zerosInd]:
                        zerosInd+=1
                    if zerosInd<len(zeros):
                        arr[zeros[zerosInd]]+=1
                        num-=1
                        arr[ind]-=1
                        zerosInd+=1
                        ops+=1
                ops+=num
                arr[ind]-=num
    print(ops)
            
