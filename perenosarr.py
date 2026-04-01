def sl(k, n):
    if k + 1 > 2*n:
        return 1
    else:
        return k+1

n = int(input())
arr = list(map(int, input().split()))
sp = []
for i in range(1, n):
    if sl(arr[i], n) - sl(arr[i-1], n) != 2:
        sp.append(i)

if sl(arr[0], n) - sl(arr[-1], n) != 2:
    sp.append(0)

if len(sp) == 0:
    k = m = 0
elif len(sp) == 1:
    k = m = sp[0] + 1
else:
    sp.sort()
    k, m = sp[0], sp[1]


print(k, m)

