class Solution:
    def temp_var(self, num: int, nums: set[int], sequences: dict[int: int]):
        temp = num + 1
        while temp in nums:
            sequences[temp] = sequences[temp - 1] + 1
            temp += 1
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        sequences = {}
    
        for num in nums:
            if num - 1 not in nums:
                sequences[num] = 1
                self.temp_var(num, nums, sequences)
            elif num - 1 in sequences:
                sequences[num] = sequences[num - 1] + 1
                self.temp_var(num, nums, sequences)
                

        return max([*sequences.values()])