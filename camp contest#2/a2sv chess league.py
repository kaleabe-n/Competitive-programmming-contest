n,k = [int(x) for x in input().split()]
players = [[[int(x),i]] for i,x in enumerate(input().split())]
 
def recur(players):
    if len(players) == 1:
        return players[0]
    newPlayers = []
    for i in range(0,len(players),2):
        temp = []
        for p in players[i]:
            if p[0] >= players[i+1][0][0]-k:
                temp.append(p)
        for p in players[i+1]:
            if p[0] >= players[i][0][0]-k:
                temp.append(p)
        temp.sort()
        newPlayers.append(temp)
        
    return recur(newPlayers)
    
ans = recur(players)
ans.sort(key=lambda x:x[1])
print(*[x[1]+1 for x in ans])
