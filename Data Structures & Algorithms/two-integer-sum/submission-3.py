class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_index:
                return [nums_index[complement], i]

            nums_index[num] = i