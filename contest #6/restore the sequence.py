    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = [int(x) for x in input().split()]
        left = 0
        right = len(seq)-1
        ans = []
        while right >= left:
            if left == right:
                ans.append(str(seq[left]))
            else:
                ans.append(str(seq[left]))
                ans.append(str(seq[right]))
            left += 1
            right -= 1
        print(" ".join(ans))
