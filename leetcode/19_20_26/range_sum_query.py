class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = nums
        pr = 0
        pref = [0]
        for el in nums:
            pr += el
            pref.append(pr)
        self.pref = pref

        # более короткое создание префиксов
        # for num in nums:
        #     self.pref.append(self.pref[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right+1] - self.pref[left]

obj = NumArray([-2, 0, 3, -5, 2, -1])

print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3