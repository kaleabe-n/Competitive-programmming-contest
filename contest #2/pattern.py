count = int(input())
words = []
for i in range(count):
    words.append(input())
ans = []
for j in range(len(words[0])):
    temp = words[0][j]
    for i in range(1,count):
        if words[i][j] != temp and words[i][j]!="?" and temp!="?":
            ans.append("?")
            break
        elif temp == "?" and words[i][j] != "?":
            temp = words[i][j]
    else:
        if temp == "?":
            ans.append("x")
        else:
            ans.append(temp)
 
print("".join(ans))
