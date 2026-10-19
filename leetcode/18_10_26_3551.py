# 3551. Minimum Swaps to Sort by Digit Sum

# You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

# Return the minimum number of swaps required to rearrange nums into this sorted order.

# A swap is defined as exchanging the values at two distinct positions in the array.

from typing import List


def digit_sum(x):
    return sum(int(d) for d in str(x))

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sum_st = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {}

        for i, num in enumerate(sum_st):
            pos[num] = i

        n = len(nums)
        visited = [False] * n

        swaps = 0

        for i in range(n):
            if visited[i]:
                continue
            j = i
            cycle_size = 0
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1
            swaps += cycle_size - 1

        return swaps