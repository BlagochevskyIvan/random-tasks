def max_sum_subarray(nums: list[int], k: int) -> int:
    mx = cur_sum = sum(nums[i] for i in range(k))
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i-k]
        mx = max(mx, cur_sum)
    return mx

assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
assert max_sum_subarray([-5, -2, -3], 2) == -5
assert max_sum_subarray([1, 2, 3, 4, 5], 1) == 5


