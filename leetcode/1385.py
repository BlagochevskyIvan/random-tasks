from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        a = 0
        for num in arr1:
            i = bisect_left(arr2, num)
            if i < len(arr2) and abs(arr2[i] - num) <= d:
                continue
            if i > 0 and abs(arr2[i - 1] - num) <= d:
                continue
            a += 1
        return a