def threeSum(self, nums: list[int]) -> list[list[int]]:
    a = sorted(nums)
    l = len(nums)
    res = []
    for i in range(l-2):
        if i > 0 and a[i] == a[i-1]:
            continue
        p1 = i + 1
        p2 = l - 1
        while p1 < p2:
            cur = a[i] + a[p1] + a[p2]
            if cur < 0:
                p1 += 1
            elif cur > 0:
                p2 -= 1
            else:
                res.append([a[i], a[p1], a[p2]])
                p1+=1
                p2-=1
                while p1 < p2 and a[p1] == a[p1-1]:
                    p1+= 1
                while p1 < p2 and a[p2] == a[p2+1]:
                    p2 -= 1
    return res