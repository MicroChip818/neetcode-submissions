class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return sorted(nums) != sorted(list(set(nums)))
        