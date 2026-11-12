n, k= map(int, input().split())
ar = list(map(int, input().split()))
sm = wd_sm = sum(ar[:k])
st = 1
for i in range(k, n):
     wd_sm+=ar[i]-ar[i-k]
     if sm < wd_sm:
          st = i-k+2
          sm = wd_sm
print(st, sm)