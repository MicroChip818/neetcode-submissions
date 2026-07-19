class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if target - num in nums_index:
                return [nums_index[diff], i]
            nums_index[num] = i

        