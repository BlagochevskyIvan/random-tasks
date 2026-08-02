import heapq

a, b, n = map(int, input().split())
conds = []

for i in range(n):
    x, y = map(int, input().split())
    back_pr = x - y
    conds.append((back_pr, x, y))
conds.sort(reverse=True)

left = [-10 ** 30] * (n + 1)
right = [-10 ** 30] * (n + 1)
if a == 0:
    left[0] = 0
if b == 0:
    right[n] = 0
hp = []
s = 0

for i in range(n):
    x = conds[i][1]
    heapq.heappush(hp, x)
    s += x
    if len(hp) > a:
        s -= heapq.heappop(hp)
    if len(hp) == a:
        left[i + 1] = s

hp = []
s = 0

for i in range(n - 1, -1, -1):
    y = conds[i][2]
    heapq.heappush(hp, y)
    s += y
    if len(hp) > b:
        s -= heapq.heappop(hp)
    if len(hp) == b:
        right[i] = s
ans = 0

for i in range(n + 1):
    ans = max(ans, left[i] + right[i])
print(ans)