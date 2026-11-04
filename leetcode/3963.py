class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = ["."*n]
        de = "#"*(n-1) + "."
        for i in range(m-1):
            ans.append(de)
        return ans