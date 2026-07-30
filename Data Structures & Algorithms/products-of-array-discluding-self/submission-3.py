import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        pre[0] = suf[-1] = 1

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
        print(pre)
        
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        print(suf)

        res = []
        for i, _ in enumerate(nums):
            res.append(pre[i] * suf[i])

        return res