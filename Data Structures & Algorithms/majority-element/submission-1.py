class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        freq_map = {}
        n = len(nums)

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
                if freq_map[num] > n / 2:
                    return num
            else:
                freq_map[num] = 1