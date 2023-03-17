num = [int(x) for x in input()]
ans = []
for n in num:
    curr = min(n,9-n)
    if len(ans) == 0 and curr == 0:
        ans.append(str(9))
    else:
        ans.append(str(curr))


print("".join(ans))
