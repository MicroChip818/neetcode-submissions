from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        res = len(nums) * [0]

        if zeros >= 2:
            return res
        elif zeros == 1:
            zero_index = nums.index(0)
            nums.remove(0)
            product = prod(nums)
            res[zero_index] = product
            return res

        product = prod(nums)
        for i, num in enumerate(nums):
            res[i] += int(product / num)

        return res