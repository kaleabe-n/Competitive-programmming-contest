testCount = int(input())
for _ in range(testCount):
    prev = ""
    seq = input()
    count = 1
    counts = {}
    for letter in seq:
        if prev == letter:
            count+=1
        else:
            if count %2 == 1:
                count = 1
            if prev in counts and prev is not None:
                counts[prev] = min(count,counts[prev])
            elif prev is not None:
                counts[prev] = count
            count = 1
        prev = letter
    if count %2 == 1:
        count = 1
    if prev in counts and prev is not None:
        counts[prev] = min(count,counts[prev])
    elif prev is not None:
        counts[prev] = count
    workingKeys = [x for x in counts if counts[x] == 1]
    workingKeys.sort()
    if len(workingKeys)>=1:
        print("".join(workingKeys))
    else:
        print()
 
