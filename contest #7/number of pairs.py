n = int(input())
boys = [int(x) for x in input().split()]
m = int(input())
girls = [int(x) for x in input().split()]
boys.sort()
girls.sort()
i = 0
j = 0
pairCount = 0
while i<len(boys) and j<len(girls):
    if abs(boys[i]-girls[j]) <=1:
        pairCount+=1
        i+=1
        j+=1
    elif boys[i]<girls[j]:
        i+=1
    else:
        j+=1
        
print(pairCount)
