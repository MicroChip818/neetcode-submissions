class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - num
            for j, num in enumerate(nums[i + 1:], start=i + 1):
                if num == complement:
                    return [i, j]