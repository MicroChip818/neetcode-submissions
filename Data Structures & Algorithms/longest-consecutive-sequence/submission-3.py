class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums = set(nums)
        lengths = {}

        for num in nums:
            if num - 1 not in nums and num not in lengths:
                sequence = [num]
                curr = num

                while curr + 1 in nums: 
                    sequence.append(curr)
                    lengths[curr] = [curr]
                    curr += 1

                lengths[num] = sequence

        return max([len(length) for length in lengths.values()])