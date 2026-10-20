class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mn = float("inf")
        mx_del = 0
        for el in prices:
            mn = min(mn, el)
            mx_del = max(mx_del, el-mn)
        return mx_del