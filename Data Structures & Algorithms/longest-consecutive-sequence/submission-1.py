class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums = sorted(list(set(nums)))
        res, temp = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
        
        return max(res, temp)