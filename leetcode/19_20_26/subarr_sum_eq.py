from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        pr_sm = {0: 1}
        res=0
        for num in nums:
            cur_sum += num
            prev_sum = cur_sum - k
            if prev_sum in pr_sm:
                res += pr_sm[prev_sum]
            if cur_sum not in pr_sm:
                pr_sm[cur_sum] = 1
            else:
                pr_sm[cur_sum] = pr_sm[cur_sum] + 1
        return res


            