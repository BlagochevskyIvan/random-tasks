from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        i = nums[-1]
        for j in range(1, 1+i):
            arr.append(j)
        for elem in nums:
            arr.remove(elem)
        return arr

        
        