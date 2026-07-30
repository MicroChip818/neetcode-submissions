class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        res = 0
        ans = 0
        for i, num in enumerate(nums):
            if i == 0:
                res = 1
                continue
            if nums[i - 1] == num - 1:
                res += 1
            else:
                ans = max(res, ans)
                res = 1

        return max(res, ans)