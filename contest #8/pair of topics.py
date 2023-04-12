n = int(input())
t = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
diff = [0] * n

for i in range(n):
    diff[i] = t[i] - s[i]

diff.sort()

total = 0
l = 0
r = n - 1

while r >= l:
    while l < r and diff[l] + diff[r] <= 0:
        l += 1

    total += max(r - l, 0)
    r -= 1

print(total)
