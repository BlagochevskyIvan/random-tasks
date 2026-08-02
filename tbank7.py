n = int(input())
s = input().strip()
symbols = "TOI"
dp = [[0] * n for i in range(n)]

for i in range(n):
    if s[i] in symbols:
        dp[i][i] = 0
    else:
        dp[i][i] = 1

for length in range(2, n + 1):
    for l_i in range(n - length + 1):
        r_i = l_i + length - 1
        ans = min(
            dp[l_i + 1][r_i] + 1,
            dp[l_i][r_i - 1] + 1
        )

        pair = 10 ** 9

        for c in symbols:
            cost = 0
            if s[l_i] != c:
                cost += 1
            if s[r_i] != c:
                cost += 1

            pair = min(pair, cost)
        if l_i + 1 <= r_i - 1:
            ans = min(ans, dp[l_i + 1][r_i - 1] + pair)
        else:
            ans = min(ans, pair)
        dp[l_i][r_i] = ans

print(dp[0][n-1])