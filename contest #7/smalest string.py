    t = int(input())
    for _ in range(t):
        n,m,k = [int(x) for x in input().split()]
        a = list(input())
        b = list(input())
        a.sort(reverse=True)
        b.sort(reverse=True)
        state = None
        ans = []
        count = 0
        while a and b:
            if ord(b[-1])<ord(a[-1]):
                if count == k and state == "b":
                    ans.append(a.pop())
                    state = "a"
                    count = 1
                else:
                    ans.append(b.pop())
                    if state == "b":
                        count+=1
                    else:
                        state = "b"
                        count = 1
            elif ord(b[-1])>ord(a[-1]):
                if count == k and state == "a":
                    ans.append(b.pop())
                    state = "b"
                    count = 1
                else:
                    ans.append(a.pop())
                    if state == "a":
                        count+=1
                    else:
                        state = "a"
                        count = 1
                
        print("".join(ans))
