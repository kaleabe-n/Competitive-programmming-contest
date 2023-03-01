n,m = [int(x) for x in input().split()]
served = [int(x) for x in input().split()]
costs = [int(x) for x in input().split()]
dishes = []
for i,cost in enumerate(costs):
    dishes.append([cost,served[i],i])
indices = [0]*n
dishes.sort(key=lambda x:x[0])
for i,j in enumerate(dishes):
    indices[j[-1]] = i
minCostInd = 0
for i in range(m):
    customerCost = 0
    food,count = [int(x) for x in input().split()]
    available = dishes[indices[food-1]][1]
    if available >= count:
        dishes[indices[food-1]][1]-=count
        customerCost += count*dishes[indices[food-1]][0]
    else:
        dishes[indices[food-1]][1] = 0
        customerCost += available*dishes[indices[food-1]][0]
        count-=available
        brocken = False
        while count>0:
            while minCostInd<n and dishes[minCostInd][1]==0:
                minCostInd+=1
            else:
                if minCostInd == n:
                    brocken = True
                    customerCost = 0
                    break
                customerCost += min(dishes[minCostInd][1],count) * dishes[minCostInd][0]
                tempCount = count
                count -= min(dishes[minCostInd][1],count)
                dishes[minCostInd][1]-=min(dishes[minCostInd][1],tempCount)
            if brocken:
                break
    print(customerCost)
