class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[-1]
        moves = 0
        for elem in nums:
            moves += x-elem
        return moves

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)