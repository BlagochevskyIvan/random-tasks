from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = nums.sort()
        arr = []
        i = range(nums[::-1])
        for j in range(i):
            arr.append(j)
        for elem in nums:
            arr.remove(elem)
        return arr

        
        