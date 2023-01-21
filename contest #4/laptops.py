    laptopsCount = int(input())
    laptops = []
    for _ in range(laptopsCount):
        price,quality = [int(x) for x in input().split()]
        laptops.append([price,quality])
    laptops.sort(key = lambda x:x[0])
     
     
    maxx = float("-inf")
    for l in laptops:
        if l[1] < maxx:
            print("Happy Alex")
            break
        maxx = max(maxx,l[1])
    else:
        print("Poor Alex")
