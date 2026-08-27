class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        zeros = nums.count(0)
        res = length * [0]

        if zeros == 1:
            zero_index = nums.index(0)
            nums.remove(0)
            prod = 1
            for num in nums:
                prod *= num
            res[zero_index] = prod

        elif zeros == 0:
            prefix = length * [1]
            pre_prod = 1
            for i in range(0, length - 1):
                pre_prod *= nums[i]
                prefix[i + 1] *= pre_prod

            postfix = length * [1]
            post_prod = 1
            for i in range(length - 1, 0, -1):
                post_prod *= nums[i]
                postfix[i - 1] *= post_prod

            for i in range(length):
                res[i] += prefix[i] * postfix[i]

        return res