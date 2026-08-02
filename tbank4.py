n, x = map(int, input().split())
nums = list(map(int, input().split()))
cm0 = 0
cmper = 10 ** 30

for i in range(n - 1):
    base = nums[i + 1] // nums[i]
    digit = (x // nums[i]) % base
    ncm0 = min(cm0 + digit, cmper + digit + 1)
    ncmper = min(cm0 + base - digit, cmper + base - digit - 1)
    cm0, cmper = ncm0, ncmper

last = x // nums[-1]
ans = min(cm0 + last, cmper + last + 1)

print(ans)