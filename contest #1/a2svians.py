    nameCount = int(input())
    names = input().split()
    flaggedNames = set(input().split())
    count = 0
    for name in names:
        if name in flaggedNames:
            continue
        else:
            lettersCount = {}
            for letter in name:
                if letter in lettersCount:
                    lettersCount[letter]+=1
                else:
                    lettersCount[letter] = 1
            temp = lettersCount[name[0]]
            for letter in lettersCount:
                if lettersCount[letter]!=temp:
                    break
            else:
                count+=1
    print(count)
