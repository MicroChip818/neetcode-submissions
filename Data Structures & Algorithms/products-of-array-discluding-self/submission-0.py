import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        if nums.count(0) == 1:
            zeroes = [0] * (len(nums) - 1)
            zero_index = nums.index(0)
            nums.remove(0)

            zeroes.insert(zero_index, math.prod(nums))
            return zeroes
        
        prod = math.prod(nums)
        res = []
        for num in nums:
            res.append(int(prod/num))
        
        return res