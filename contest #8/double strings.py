testCount = int(input())
for _ in range(testCount):
    strs = []
    n = int(input())
    for _ in range(n):
        strs.append(input())
    strsSet = set(strs)
    ans = []
    for word in strs:
        for i in range(1,len(word)):
            firstHalf = word[:i]
            secondHalf = word[i:]
            if firstHalf in strsSet and secondHalf in strsSet:
                ans.append('1')
                break
        else:
            ans.append('0')
    print("".join(ans))
