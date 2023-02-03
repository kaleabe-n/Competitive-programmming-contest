testCount = int(input())
for _ in range(testCount):
    s = input()
    left = 0
    right = 0
    window = {"1":0,"2":0,"3":0}
    minLen = float('inf')
    while right < len(s):
        if 0 in window.values():
            window[s[right]] += 1
            right += 1
        else:
            window[s[left]] -= 1
            left +=1
        if 0 not in window.values():
            minLen = min(minLen,right-left)
    while 0 not in window.values() and left < len(s):
        window[s[left]] -= 1
        left +=1
        if 0 not in window.values():
            minLen = min(minLen,right-left)
            
    if minLen == float('inf'):
        print(0)
    else:
        print(minLen)
