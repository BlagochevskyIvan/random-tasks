def two_sum(nums: list[int], target: int) -> list[int]:
    #словарь где ключ это число а значение это его индекс
    d = {}
    for i in range(len(nums)):
        chis = nums[i]
        nuzh = target-chis
        if nuzh in d:
            return [d[nuzh], i]
        else:
            d.setdefault(chis, i)