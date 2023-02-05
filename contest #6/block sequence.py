n,m = [int(x) for x in input().split()]
stacks = [int(x) for x in input().split()]
stacks.sort()
extras = 0
prev = 0
removed = 0
for s in stacks:
    curr = s-prev
    if s!=0 and curr==0:
        if extras > 0:
            extras -= 1
            removed += s
        else:
            removed += s-1
    elif s == 0:
        pass
    elif curr > 0:
        extras += curr -1
        removed += s-curr
    prev = s
print(removed)
