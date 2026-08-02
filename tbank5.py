n, m = map(int, input().split())
de = 10**9 + 7

f = m * (m - 1) % de
nxt = (m - 1 + (m - 2)**2) % de
print(f * pow(nxt, n - 1, de) % de)