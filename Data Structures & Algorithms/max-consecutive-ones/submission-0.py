class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        for num in nums:
            if num == 0:
                max_ones = curr_ones if curr_ones > max_ones else max_ones
                curr_ones = 0
                continue
            curr_ones += 1
        return max(max_ones, curr_ones)
            
                