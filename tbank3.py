n = int(input())
d = list(map(int, input().split())) 

left = [0] * n
mn = d[0]
right = [0] * n
mx = d[n-1]

ans = 0
for i in range(1, n):
     mn = min(mn, d[i])
     left[i] = max(left[i-1], d[i] - mn)

for i in range(n-2, -1, -1):
    mx = max(mx, d[i])
    right[i] = max(right[i+1], mx - d[i])

for i in range(n):
     ans = max(ans, left[i] + right[i])
print(ans)