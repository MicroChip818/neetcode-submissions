class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = l * [0]
        pre, post = 1, 1

        for i in range(l):
            res[i] = pre
            pre *= nums[i]

        for i in range(l - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res