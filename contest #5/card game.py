n = int(input())
cards = [int(x) for x in input().split()]
s = 0
d = 0
sTurn = True
left = 0
right = len(cards)-1
while left <= right:
    if cards[left] > cards[right]:
        best = cards[left]
        left += 1
    else:
        best = cards[right]
        right -= 1
    if sTurn:
        s+=best
    else:
        d+=best
    sTurn = not sTurn
print(s,d)
