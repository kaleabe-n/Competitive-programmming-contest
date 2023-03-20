n,d = [int(x) for x in input().split()]
players = [int(x) for x in input().split()]
players.sort()
l = 0
r = n-1
currSum = 0
rAdded = False
wins = 0
while l<=r:
    if not rAdded:
        rAdded = True
    elif l==r:
        l+=1
        continue
    else:
        l+=1
    currSum+=players[r]
    if currSum>d:
        wins += 1
        r -= 1
        currSum=0
        rAdded = False

print(wins)
